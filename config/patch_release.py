import yaml
import sys



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("{} OLD_RELEASES NEW_RELEASES".format(sys.argv[0]))
        sys.exit(1)
    
    new_cfg = None
    old_cfg = None
    new_cfg_path = sys.argv[1]
    old_cfg_path = sys.argv[2]

    try:
        new_cfg = yaml.safe_load(open(new_cfg_path))
        old_cfg = yaml.safe_load(open(old_cfg_path))
    except Exception as e:
        print("Error on loading yaml files {}".format(e))
        sys.exit(1)
    

    for key in new_cfg.keys():
        old_cfg.setdefault(key, {})
        old_cfg[key] = new_cfg[key]
    
    patched_cfg_name = "{}.patch".format(old_cfg_path)
    patched_cfg = open(patched_cfg_name, "w")
    patched_cfg.write(yaml.dump(old_cfg))
    patched_cfg.close()

    print("Saved as {}".format(patched_cfg_name))
