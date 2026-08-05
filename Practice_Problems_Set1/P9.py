def create_hero(name, *powers, **stats):
    avg=0;
    print(f"Hero: {name}")
    print("Powers:")
    print("Powers:",", ".join(powers))
    
    for key,value in stats.items():
        print(f"{key}: {value}")
        avg+=value/len(stats)
    if avg>=90:
        print(f"Overall Rating: {avg:.1f}->S Tier")
    else:
        print(f"Overall Rating: {avg:.1f}")

create_hero("Spider-Man", "wall-crawl","spider-sense",strength=85, agility=95,intelligence=92)




