time_for_pic = int(input())
scene = int(input())
time_scene = int(input())


pitch = time_for_pic * 0.15
time_for_scene = scene * time_scene
total_time = pitch + time_for_scene

diff = abs(time_for_pic - total_time)

if time_for_pic <= total_time:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")