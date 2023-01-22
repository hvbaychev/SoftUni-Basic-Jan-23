volume_of_pool = int(input())
flow_pipe_one = int(input())
flow_pipe_two = int(input())
hours_missing_worker = float(input())

first_pipe_volume = flow_pipe_one * hours_missing_worker
second_pipe_volume = flow_pipe_two * hours_missing_worker

total_volume_after_fillup = first_pipe_volume + second_pipe_volume

if total_volume_after_fillup <= volume_of_pool:
    first_pipe_flow = (first_pipe_volume / total_volume_after_fillup) * 100
    second_pipe_flow = (second_pipe_volume / total_volume_after_fillup) * 100
    pool_field = total_volume_after_fillup / volume_of_pool * 100
    print(f"The pool is {pool_field:.2f}% full. Pipe 1: {first_pipe_flow:.2f}%. Pipe 2: {second_pipe_flow:.2f}%.")
else:
    print(f"For {hours_missing_worker:.2f} hours the pool overflows with {(total_volume_after_fillup - volume_of_pool):.2f} liters.")


