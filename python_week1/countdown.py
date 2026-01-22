#countdown script

from tracemalloc import start


weeks_left = 8
days_per_week = 7

total_days = weeks_left * days_per_week

total_hours = total_days * 24

print("Only " + str(total_days) +  " or " + str(total_hours) + " hours left til ML course!")


epoch = 1 
total_epoch = 100
loss = 0.456
accuracy = 0.892

print(f'Epoch {epoch}/{total_epoch}:')
print(f'Loss: {loss:.3f}')
print(f'Accuracy: {accuracy:.1%}')