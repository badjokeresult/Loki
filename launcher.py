import loki

if __name__ == "__main__":
    args = loki.main()
    args.update = True
    loki.start_scanning(args)
    args.update = False
    args.allhds = True
    args.allreasons = True
    args.scriptanalysis = True
    args.intense = True
    args.pesieveshellc = True
    loki.start_scanning(args)

