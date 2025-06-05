# Import built-in modules
from collections import defaultdict
import json
import os

# Import local modules
import unreal

DIR = os.path.dirname(os.path.abspath(__file__))

def unreal_progress(tasks, label="����", total=None):
    total = total if total else len(tasks)
    with unreal.ScopedSlowTask(total, label) as task:
        task.make_dialog(True)
        for i, item in enumerate(tasks):
            if task.should_cancel():
                break
            task.enter_progress_frame(1, "%s %s/%s" % (label, i, total))
            yield item


def main():
    # NOTE: ��ȡ sequence
    unreal.log("Exported {0} to {1}".format(name, export_path))
    sequence = unreal.load_asset('/Game/RecSeq')
    # NOTE: �ռ� sequence �������е� binding
    binding_dict = defaultdict(list)
    for binding in sequence.get_bindings():
        binding_dict[binding.get_name()].append(binding)

    # NOTE: ��������Ϊ Face �� binding
    for binding in unreal_progress(binding_dict.get("BP_FlyingPawn", []), "Face"):
        # NOTE: ��ȡ�ؼ�֡ channel ����
        keys_dict = {}
        for track in binding.get_tracks():
            for section in track.get_sections():
                for channel in unreal_progress(section.get_channels(), "KeyFrame"):
                    if not channel.get_num_keys():
                        continue
                    keys = []
                    for key in channel.get_keys():
                        frame_time = key.get_time()
                        frame = frame_time.frame_number.value + frame_time.sub_frame
                        keys.append({"frame": frame, "value": key.get_value()})

                    keys_dict[channel.get_name()] = keys

        # NOTE: ���� json
        name = binding.get_parent().get_name()
        export_path = os.path.join(DIR, "{0}.json".format(name))
        with open(export_path, "w") as wf:
            json.dump(keys_dict, wf, indent=4)
        
