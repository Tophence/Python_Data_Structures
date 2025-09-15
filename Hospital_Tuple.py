#Immutable Hospital Layout -Fixed coordinates for critical stations
# Emergency Exit Locations (Floor, X, Y)
emergency_exits = (
    ("Main Lobby", 1, 12.5),
    ("ER Back", 1, 87.3),
    ("ICU Wing", 3, 45.0)
)

# Access data
print("Exit near ICU:", emergency_exits[2][0])  # ICU Wing & the [0] means change nothing about it 
print("Exit near Emergency room:", emergency_exits[1][0]) # ER back
print("Exit near the lobby:", emergency_exits[0][0]) # Main lobby

# Try to modify (will fail)
try:
    emergency_exits[1] = ("Lab Zone", 2, 33.1)
except TypeError as e:
    print("Security Alert! ", e) 
    # Output: 'tuple' object does not support item assignment