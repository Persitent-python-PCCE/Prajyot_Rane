def launch(*stages, abort_threshold=5000):
    total=0
    i=1
    for s in stages:
            total+=s
            print(f"Stage {i} armed --> cumulative {total} kg")
            if total>abort_threshold:
                print(f"[ABORT] at stage {i}: threshold 5000 kg exceeded.")
                break;   
            i+=1
launch(1200, 1800, 2500, 900)