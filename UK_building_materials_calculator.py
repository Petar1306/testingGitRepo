# UK Building Materials Calculator 🏗️
import math


def fence_calculator():
    """Calculate materials for fencing (British standards)"""
    print("\n🌲 Fence Calculator (UK Standards)")
    try:
        length = float(input("Enter fence length (m): "))
        height = float(input("Enter fence height (m): "))

        # Standard UK fence panel dimensions (1800mm wide)
        panel_width = 1.8
        panels_needed = math.ceil(length / panel_width)

        # Posts every 1.8m + end posts
        posts_needed = math.ceil(length / panel_width) + 1

        # Gravel boards (150mm height standard)
        gravel_boards = math.ceil(length / 1.8) if height > 1.5 else 0

        print(f"\n📝 Materials Required for {length}m × {height}m fence:")
        print(f"• Fence panels (1.8m wide): {panels_needed}")
        print(f"• Wooden posts (100×100mm): {posts_needed}")
        print(f"• Concrete for post bases: {posts_needed * 0.025}m³")
        if gravel_boards:
            print(f"• Gravel boards (150mm): {gravel_boards}")
        print(f"• Postfix concrete: {posts_needed * 20}kg")
    except ValueError:
        print("Invalid input! Please enter numbers.")


def decking_calculator():
    """Calculate decking materials (British standards)"""
    print("\n🪵 Decking Calculator (UK Standards)")
    try:
        area = float(input("Enter decking area (m²): "))
        board_length = float(input("Enter board length (m, typically 3.6m): "))
        board_width = float(input("Enter board width (mm, typically 140mm): ")) / 1000

        # Calculate boards
        boards_needed = math.ceil(area / (board_length * board_width)) * 1.1  # +10% waste

        # Frame (joists at 400mm centres)
        perimeter = math.sqrt(area) * 4  # Approximation
        joists_needed = math.ceil(area / 0.4)  # 400mm spacing

        print(f"\n📝 Materials Required for {area}m² decking:")
        print(f"• Deck boards ({board_length}m × {board_width * 1000}mm): {round(boards_needed)}")
        print(f"• Joists (400mm centres): {joists_needed} × 3.6m lengths")
        print(f"• Frame timber: {round(perimeter)}m of 150×50mm treated timber")
        print(f"• Screws: {round(area * 20)} (20 per m²)")
    except ValueError:
        print("Invalid input! Please enter numbers.")


def brickwork_calculator():
    """Calculate brickwork materials (UK standards)"""
    print("\n🧱 Brickwork Calculator (UK Standards)")
    try:
        area = float(input("Enter wall area (m²): "))
        brick_type = input("Standard brick size (215×102.5×65mm)? (y/n): ").lower()

        if brick_type == 'y':
            bricks_per_m2 = 60  # Standard UK brick
            mortar_per_m2 = 0.026  # m³
        else:
            bricks_per_m2 = float(input("Enter bricks per m²: "))
            mortar_per_m2 = float(input("Enter mortar per m² (m³): "))

        total_bricks = math.ceil(area * bricks_per_m2 * 1.05)  # +5% waste
        total_mortar = area * mortar_per_m2

        print(f"\n📝 Materials Required for {area}m² brickwork:")
        print(f"• Bricks: {total_bricks} (standard UK size)")
        print(f"• Mortar (1:5 mix): {round(total_mortar, 3)}m³")
        print(f"• Cement: {round(total_mortar * 7)} bags")
        print(f"• Building sand: {round(total_mortar * 0.6, 2)}m³")
        print(f"• Plasticiser: {round(area * 0.1)}L (100ml per m²)")
    except ValueError:
        print("Invalid input! Please enter numbers.")


def tiling_calculator():
    """Calculate tiling materials (British standards)"""
    print("\n🧱 Tiling Calculator (UK Standards)")
    try:
        area = float(input("Enter area to tile (m²): "))
        tile_type = input("Tile type (floor/wall/slab): ").lower()

        if tile_type == 'floor':
            adhesive_per_m2 = 4  # kg
            grout_per_m2 = 0.5  # kg
        elif tile_type == 'wall':
            adhesive_per_m2 = 3.5
            grout_per_m2 = 0.4
        else:  # slabs
            adhesive_per_m2 = 6
            grout_per_m2 = 0

        tile_size = input("Enter tile size (mm, e.g., 300x300): ")
        w, h = map(float, tile_size.lower().split('x'))
        tile_area = (w / 1000) * (h / 1000)

        tiles_needed = math.ceil(area / tile_area * 1.1)  # +10% waste

        print(f"\n📝 Materials Required for {area}m² {tile_type} tiling:")
        print(f"• Tiles ({tile_size}mm): {tiles_needed}")
        print(f"• Adhesive: {round(area * adhesive_per_m2)}kg")
        if grout_per_m2 > 0:
            print(f"• Grout: {round(area * grout_per_m2)}kg")
    except:
        print("Invalid input! Format: 300x300")


def concrete_calculator():
    """Calculate concrete materials (UK standards)"""
    print("\n🏗️ Concrete Calculator (UK Standards)")
    try:
        volume = float(input("Enter volume needed (m³): "))
        usage = input("Usage (foundation/slab/column): ").lower()

        if usage == 'foundation':
            mix = (1, 3, 6)  # 1:3:6 (ST2 - Gen purpose)
            strength = "ST2 (10N/mm²)"
        elif usage == 'slab':
            mix = (1, 2, 4)  # 1:2:4 (ST3 - Light duty)
            strength = "ST3 (15N/mm²)"
        else:  # column
            mix = (1, 1.5, 3)  # 1:1.5:3 (ST4 - Heavy duty)
            strength = "ST4 (20N/mm²)"

        cement, sand, gravel = mix
        total = cement + sand + gravel
        dry_volume = volume * 1.54  # Dry mix factor

        print(f"\n📝 Materials for {volume}m³ {usage} ({strength}):")
        print(f"• Cement: {round((cement / total) * dry_volume / 0.035)} bags (25kg)")
        print(f"• Sharp sand: {round((sand / total) * dry_volume, 2)}m³")
        print(f"• Aggregate ({'10mm' if usage == 'column' else '20mm'}): {round((gravel / total) * dry_volume, 2)}m³")
    except ValueError:
        print("Invalid input! Please enter numbers.")


def main():
    print("🇬🇧 UK Building Materials Calculator")
    print("1. Fencing")
    print("2. Decking")
    print("3. Brickwork")
    print("4. Tiling")
    print("5. Concrete")
    print("6. Exit")

    while True:
        choice = input("\nChoose task (1-6): ")
        if choice == '1':
            fence_calculator()
        elif choice == '2':
            decking_calculator()
        elif choice == '3':
            brickwork_calculator()
        elif choice == '4':
            tiling_calculator()
        elif choice == '5':
            concrete_calculator()
        elif choice == '6':
            print("Cheers for using the calculator! 🍻")
            break
        else:
            print("Invalid choice! Try 1-6")


if __name__ == "__main__":
    main()
    