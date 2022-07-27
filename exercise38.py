trainees=" gopika mathew sanju Refun"
print("there are four more trainees...")
print(trainees)
split_trainees=trainees.split()
remaining_trainees=["anoop","aldrin","amal","viswajith"]
while len(split_trainees)!=8:
    next_one=remaining_trainees.pop()
    print("adding : ",next_one)
    split_trainees.append(next_one)
    print(f"there are {len(split_trainees)} now")
print(split_trainees)
print(split_trainees[0])