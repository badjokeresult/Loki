import os
import loki
import upgrader


if __name__ == "__main__":
    working_dir = "C:\\Loki"
    os.makedirs(working_dir, exist_ok=True)
    os.chdir(working_dir)
    
    upgrader_args = upgrader.main()
    upgrader_args.sigsonly = True
    upgrader.do_upgrade(upgrader_args)

    args = loki.main()
    args.allhds = True
    args.allreasons = True
    args.scriptanalysis = True
    args.intense = True
    args.pesieveshellc = True
    loki.start_scanning(args)

