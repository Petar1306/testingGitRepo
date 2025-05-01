# UK Building Materials Calculator 🏗️
import math


def fence_calculator():
    """Calculate fencing materials with post height validation"""
    print("\n🌲 Fence Calculator (UK Standards)")
    try:
        length = float(input("Enter fence length (m): "))
        panel_height = float(input("Enter panel height (m, typically 1.2-1.8m): "))
        post_height = float(input("Enter post height (m, typically 2.1-2.4m): "))

        # Validate heights
        if post_height < panel_height + 0.3:
            print("⚠️ Warning: Posts should be 300mm taller than panels")

        # Calculations
        panel_width = 1.8
        panels_needed = math.ceil(length / panel_width)
        posts_needed = math.ceil(length / panel_width) + 1
        gravel_boards = math.ceil(length / 1.8) if panel_height >= 1.2 else 0

        # Post concrete based on height (0.25m³ for 2.4m posts)
        concrete_per_post = 0.25 + (post_height - 1.8) * 0.1

        print(f"\n📝 Materials for {length}m × {panel_height}m fence:")
        print(f"• Panels (1.8m×{panel_height}m): {panels_needed}")
        print(f"• Posts ({post_height}m): {posts_needed} (100×100mm treated)")
        print(f"• Concrete: {posts_needed * concrete_per_post:.2f}m³")
        print(f"• Gravel boards: {gravel_boards}" if gravel_boards else "")

    except ValueError:
        print("Invalid input! Numbers only.")


def decking_calculator():
    """Calculate decking materials with waste allowance"""
    print("\n🪵 Decking Calculator")
    try:
        area = float(input("Enter decking area (m²): "))
        board_size = input("Enter board size (mm, e.g., 140x22): ").split('x')
        board_width, board_thickness = map(float, board_size)

        # Convert to meters
        board_area = (board_width / 1000) * 3.6  # Standard 3.6m length
        boards_needed = math.ceil(area / board_area * 1.15)  # 15% waste

        # Joists at 400mm centers
        joists_needed = math.ceil(area * 3.5)  # 3.5m per m²

        print(f"\n📝 Materials for {area}m² decking:")
        print(f"• Boards: {boards_needed} ({board_width}x{board_thickness}mm)")
        print(f"• Joists: {joists_needed}m (47×150mm at 400mm centers)")
        print(f"• Screws: {math.ceil(area * 25)} (25 per m²)")

    except:
        print("Invalid input! Use format like '140x22'")


def brickwork_calculator():
    """Calculate brick and mortar quantities"""
    print("\n🧱 Brickwork Calculator")
    try:
        area = float(input("Enter wall area (m²): "))
        brick_size = input("Brick size (mm, e.g., 215x102.5x65): ").split('x')
        width, _, height = map(float, brick_size)

        # Calculate bricks per m² including mortar joints
        bricks_per_m2 = math.ceil(1 / ((width / 1000 + 0.01) * (height / 1000 + 0.01)))
        mortar_per_m2 = 0.025  # m³

        print(f"\n📝 Materials for {area}m² brickwork:")
        print(f"• Bricks: {math.ceil(area * bricks_per_m2 * 1.1)} (10% waste)")
        print(f"• Mortar: {area * mortar_per_m2:.2f}m³ (1:5 mix)")
        print(f"• Cement: {math.ceil(area * 0.5)} bags")
        print(f"• Sand: {area * 0.1:.2f}m³")

    except:
        print("Invalid input! Use format like '215x102.5x65'")


def tiling_calculator():
    """Calculate tile and adhesive quantities"""
    print("\n🧱 Tiling Calculator")
    try:
        area = float(input("Enter area to tile (m²): "))
        tile_type = input("Type (wall/floor/slab): ").lower()
        tile_size = input("Tile size (mm, e.g., 300x300): ").split('x')

        # Different adhesives for different tile types
        adhesive_rates = {'wall': 4, 'floor': 5, 'slab': 7}  # kg/m²
        adhesive = adhesive_rates.get(tile_type, 5)

        # Calculate tiles needed
        tile_area = (float(tile_size[0]) / 1000) * (float(tile_size[1]) / 1000)
        tiles_needed = math.ceil(area / tile_area * 1.1)  # 10% waste

        print(f"\n📝 Materials for {area}m² {tile_type} tiling:")
        print(f"• Tiles: {tiles_needed} ({'x'.join(tile_size)}mm)")
        print(f"• Adhesive: {math.ceil(area * adhesive)}kg")
        if tile_type != 'slab':
            print(f"• Grout: {math.ceil(area * 0.5)}kg")

    except:
        print("Invalid input! Check your values")


def concrete_calculator():
    """Calculate concrete mix materials"""
    print("\n🏗️ Concrete Calculator")
    try:
        volume = float(input("Enter volume needed (m³): "))
        mix_type = input("Mix type (foundation/slab/column): ").lower()

        # UK standard mixes
        mixes = {
            'foundation': (1, 3, 6),  # ST2
            'slab': (1, 2, 4),  # ST3
            'column': (1, 1.5, 3)  # ST4
        }
        cement, sand, gravel = mixes.get(mix_type, (1, 2, 4))

        # Calculate materials (1.54 dry mix factor)
        cement_volume = (cement / (cement + sand + gravel)) * volume * 1.54
        sand_volume = (sand / (cement + sand + gravel)) * volume * 1.54
        gravel_volume = (gravel / (cement + sand + gravel)) * volume * 1.54

        print(f"\n📝 Materials for {volume}m³ {mix_type} concrete:")
        print(f"• Cement: {math.ceil(cement_volume / 0.035)} bags (25kg)")
        print(f"• Sand: {sand_volume:.2f}m³")
        print(f"• Aggregate: {gravel_volume:.2f}m³ ({'10mm' if mix_type == 'column' else '20mm'})")

    except ValueError:
        print("Invalid input! Numbers only")


def plastering_calculator():
    """Calculate plastering materials"""
    print("\n🪣 Plastering Calculator")
    try:
        area = float(input("Enter wall area (m²): "))
        thickness = float(input("Enter thickness (mm, typically 12-15mm): ")) / 1000

        # UK plaster mix (1:4 cement:sand)
        volume = area * thickness
        cement = volume * 1.54 * (1 / 5)  # 1 part cement
        sand = volume * 1.54 * (4 / 5)  # 4 parts sand

        print(f"\n📝 Materials for {area}m² plastering:")
        print(f"• Cement: {math.ceil(cement / 0.035)} bags (25kg)")
        print(f"• Building sand: {sand:.2f}m³")
        print(f"• Waterproofer: {math.ceil(area * 0.1)}L (for external work)")

    except ValueError:
        print("Invalid input! Numbers only")


def main():
    print("\n🇬🇧 UK Building Materials Calculator 🏗️")
    print("1. Fencing Calculator")
    print("2. Decking Calculator")
    print("3. Brickwork Calculator")
    print("4. Tiling Calculator")
    print("5. Concrete Calculator")
    print("6. Plastering Calculator")
    print("7. Exit")

    while True:
        choice = input("\nChoose calculator (1-7): ")

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
            plastering_calculator()
        elif choice == '7':
            print("\nThank you for using the calculator! 👷")
            break
        else:
            print("Invalid choice! Please enter 1-7")


if __name__ == "__main__":
    main()
