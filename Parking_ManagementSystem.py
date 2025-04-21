import heapq

class Vehicle:
    def __init__(self, var_type, var_priority=False):
        self.var_type = var_type
        self.var_priority = var_priority

class Slot:
    def __init__(self, z, l, n, t, r=False):
        self.var_zone, self.var_level, self.var_number = z, l, n
        self.var_type, self.var_reserved = t, r
        self.var_occupied, self.var_vehicle = False, None

    def __lt__(self, other):
        return (self.var_zone, self.var_level, self.var_number) < (other.var_zone, other.var_level, other.var_number)

class ParkingSystem:
    def __init__(self):
        self.var_slots = []
        self.var_available = {"Bike": [], "Car": [], "Truck": []}
        self.var_reserved = []
        self.var_parked_list = []  
        self.create_slots()

    def create_slots(self):
        for z in ['A', 'B', 'C']:
            for l in range(1, 4):
                for n in range(1, 11):
                    t = "Bike" if n <= 3 else "Car" if n <= 7 else "Truck"
                    r = (n == 1)
                    slot = Slot(z, l, n, t, r)
                    self.var_slots.append(slot)
                    if r:
                        self.var_reserved.append(slot)
                    else:
                        heapq.heappush(self.var_available[t], slot)

    def park_vehicle(self, v):
        if v.var_priority:
            for s in self.var_reserved:
                if s.var_type == v.var_type and not s.var_occupied:
                    self.assign_slot(s, v)
                    return
            print("No reserved slot available.")
        else:
            while self.var_available[v.var_type]:
                s = heapq.heappop(self.var_available[v.var_type])
                if not s.var_occupied:
                    self.assign_slot(s, v)
                    return
            print("No available slot.")

    def assign_slot(self, s, v):
        s.var_occupied, s.var_vehicle = True, v
        self.var_parked_list.append((v, s))
        print(f"Allocated Slot: Zone {s.var_zone} - Level {s.var_level} - Slot {s.var_number}")

    def remove_vehicle(self, v_id):
        for i, (v, s) in enumerate(self.var_parked_list):
            if id(v) == v_id:
                s.var_occupied = False
                s.var_vehicle = None
                if not s.var_reserved:
                    heapq.heappush(self.var_available[s.var_type], s)
                self.var_parked_list.pop(i)
                print("Vehicle removed successfully.")
                return
        print("Vehicle ID not found.")

    def show_all_slots(self):
        for s in self.var_slots:
            status = "Occupied" if s.var_occupied else "Available"
            tag = "[Reserved]" if s.var_reserved else ""
            print(f"{s.var_zone}-{s.var_level}-{s.var_number} ({s.var_type}) {tag}: {status}")

    def show_reserved_slots(self):
        found = False
        for s in self.var_reserved:
            if not s.var_occupied:
                print(f"{s.var_zone}-{s.var_level}-{s.var_number}")
                found = True
        if not found:
            print("No available reserved slots.")

    def show_priority_vehicles(self):
        found = False
        for v, s in self.var_parked_list:
            if v.var_priority and s.var_reserved:
                print(f"{v.var_type} at {s.var_zone}-{s.var_level}-{s.var_number}")
                found = True
        if not found:
            print("No priority vehicles parked.")

def main():
    system = ParkingSystem()
    vehicles = []  # Stores all created vehicles

    print("Welcome to Smart City Parking System")

    while True:
        print("\n1. Park a Vehicle\n2. Remove a Vehicle\n3. Show All Parking Slots\n4. Show Available Slots for EVs\n5. Show Priority Vehicles\n6. Exit")
        c = input("Choose Option: ").strip()

        if c == "1":
            t = input("Vehicle Type (Bike/Car/Truck): ").capitalize()
            if t not in ["Bike", "Car", "Truck"]:
                print("Invalid type.")
                continue
            p = input("Priority (Y/N): ").strip().upper() == "Y"
            v = Vehicle(t, p)
            vehicles.append(v)
            system.park_vehicle(v)

        elif c == "2":
            if not vehicles:
                print("No vehicles parked.")
                continue
            print("Vehicles:")
            for v in vehicles:
                tag = " [Priority]" if v.var_priority else ""
                print(f"{id(v)}: {v.var_type}{tag}")
            try:
                vid = int(input("Enter Vehicle ID to Remove: "))
                system.remove_vehicle(vid)
                vehicles = [v for v in vehicles if id(v) != vid]
            except:
                print("Invalid input.")

        elif c == "3":
            system.show_all_slots()

        elif c == "4":
            system.show_reserved_slots()

        elif c == "5":
            system.show_priority_vehicles()

        elif c == "6":
            print("Lab completed successfully.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
