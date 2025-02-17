import copy
import os
import threading
from videotrans.configure import config
from videotrans.util import tools

lasterror = ""


# 文字合成
def text_to_speech(
        inst=None,
        text="",
        role="",
        rate='+0%',
        pitch="+0Hz",
        volume="+0%",
        language=None,
        filename=None,
        tts_type=None,
        uuid=None,
        play=False,
        set_p=True):
    global lasterror
    get_voice = None
    if tts_type == "edgeTTS":
        from .edgetts import get_voice
    elif tts_type == "AzureTTS":
        from .azuretts import get_voice
    elif tts_type == "openaiTTS":
        from .openaitts import get_voice
    elif tts_type == "clone-voice":
        from .clone import get_voice
    elif tts_type == 'TTS-API':
        from .ttsapi import get_voice
    elif tts_type == 'GPT-SoVITS':
        from .gptsovits import get_voice
    elif tts_type == 'CosyVoice':
        from .cosyvoice import get_voice
    elif tts_type == 'FishTTS':
        from .fishtts import get_voice
    elif tts_type == 'elevenlabsTTS':
        from .elevenlabs import get_voice
    elif tts_type == 'gtts':
        from .gtts import get_voice
    elif tts_type == 'ChatTTS':
        from .chattts import get_voice
    elif tts_type == '302.ai':
        from .ai302tts import get_voice

    if get_voice:
        try:
            get_voice(
                text=text,
                volume=volume,
                pitch=pitch,
                role=role,
                rate=rate,
                language=language,
                filename=filename,
                uuid=uuid,
                set_p=set_p,
                inst=inst)
        except Exception as e:
            lasterror = str(e)
    if tools.vail_file(filename):
        if play:
            threading.Thread(target=tools.pygameaudio, args=(filename,)).start()
    else:
        config.logger.error(f'no filename={filename} {tts_type=} {text=},{role=}')


# 单独处理 AzureTTS 批量
def _azuretts(queue_tts, language=None, set_p=False, inst=None,uuid=None):
    from .azuretts import get_voice
    num = int(config.settings['azure_lines'])
    qlist = [queue_tts[i:i + num] for i in range(0, len(queue_tts), num)]
    for i, q in enumerate(qlist):
        get_voice(
            text=q,
            volume=queue_tts[0]["volume"],
            pitch=queue_tts[0]["pitch"],
            role=queue_tts[0]["role"],
            rate=queue_tts[0]["rate"],
            language=language,
            uuid=uuid,
            set_p=set_p)
        if inst:
            inst.precent += 1
        tools.set_process(f"AzureTTS...", type="logs",btnkey=inst.init['btnkey'] if inst else "",uuid=uuid)


def run(*, queue_tts=None, language=None, set_p=True, inst=None,uuid=None):
    queue_tts_copy = copy.deepcopy(queue_tts)
    # 需要并行的数量3
    n_total = len(queue_tts)
    if n_total < 1:
        return False

    n = 0
    dub_nums = int(config.settings['dubbing_thread'])
    if config.exit_soft or (config.current_status != 'ing' and config.box_tts != 'ing'):
        return True
    if len(queue_tts) > 0 and queue_tts[0]['tts_type'] == 'AzureTTS':
        _azuretts(queue_tts, language=language, set_p=set_p, inst=inst,uuid=uuid)
    else:
        while len(queue_tts) > 0:
            if config.exit_soft or (config.current_status != 'ing' and config.box_tts != 'ing'):
                return True
            try:
                tolist = []
                for i in range(dub_nums):
                    if len(queue_tts) > 0:
                        p = queue_tts.pop(0)
                        if p['role'] != 'clone' and tools.vail_file(p['filename']):
                            continue
                        tolist.append(threading.Thread(target=text_to_speech, kwargs={
                            "text": p['text'],
                            "role": p['role'],
                            "rate": p['rate'],
                            "pitch": p['pitch'],
                            "volume": p['volume'],
                            "filename": p['filename'],
                            "tts_type": p['tts_type'],
                            "set_p": set_p,
                            "inst": inst,
                            "language": language
                        }))
                if len(tolist) < 1:
                    continue
                for t in tolist:
                    t.start()
                for t in tolist:
                    n += 1
                    if set_p:
                        tools.set_process(f'{config.transobj["kaishipeiyin"]} [{n}/{n_total}]',type="logs",
                                          btnkey=inst.init['btnkey'] if inst else '',uuid=uuid)
                    t.join()
            except Exception as e:
                print(f'runtts:{str(e)}')

    err = 0
    for it in queue_tts_copy:
        if not tools.vail_file(it['filename']):
            err += 1
    if err >= (n_total / 3):
        raise Exception(f'{config.transobj["peiyindayu31"]}:{lasterror if lasterror is not True else ""}')
    return True
