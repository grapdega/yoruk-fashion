extends Control

signal item_equipped(category, item)
signal item_unequipped(category)

var equipped := {}
var textures := {}
var items := {}
var gender := "female"

var body_zones := {
	"accessory": Rect2(70, 2, 110, 35),
	"hair":      Rect2(73, 30, 104, 65),
	"top":       Rect2(70, 95, 110, 75),
	"bottom":    Rect2(95, 170, 60, 70),
	"shoes":     Rect2(95, 240, 60, 22),
}

func _ready() -> void:
	var f = FileAccess.open("res://items.json", FileAccess.READ)
	if not f:
		push_error("Failed to open items.json")
		return
	var text = f.get_as_text()
	var parsed = JSON.parse_string(text)
	if parsed is Dictionary:
		items = parsed
	else:
		push_error("Failed to parse items.json")

func get_items(category: String) -> Array:
	return items.get(category, [])

func get_categories() -> Array:
	return items.keys()

func equip(category: String, item: Dictionary) -> void:
	equipped[category] = item
	queue_redraw()
	item_equipped.emit(category, item)

func unequip(category: String) -> void:
	equipped.erase(category)
	queue_redraw()
	item_unequipped.emit(category)

func is_equipped(category: String) -> bool:
	return equipped.has(category)

func get_equipped(category: String):
	return equipped.get(category, null)

func cycle_category(category: String) -> void:
	var cat_items = items.get(category, [])
	if cat_items.is_empty():
		return
	var current = equipped.get(category)
	if current == null:
		equip(category, cat_items[0])
		return
	var idx = -1
	for i in range(cat_items.size()):
		if cat_items[i]["id"] == current["id"]:
			idx = i
			break
	if idx < 0 or idx + 1 >= cat_items.size():
		unequip(category)
	else:
		equip(category, cat_items[idx + 1])

func get_texture(path: String) -> Texture2D:
	if textures.has(path):
		return textures[path]
	var tex = load(path)
	if tex:
		textures[path] = tex
	return tex

func get_char_offset() -> Vector2:
	return (size - Vector2(250, 300)) / 2

func get_draw_offset() -> Vector2:
	return Vector2(0,0)

func get_zone_at(pos: Vector2) -> String:
	for zone in body_zones:
		if body_zones[zone].has_point(pos):
			return zone
	return ""

func _gui_input(event: InputEvent) -> void:
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		var c = get_char_offset()
		var local = event.position - c
		var zone = get_zone_at(local)
		if zone:
			cycle_category(zone)
			accept_event()

func set_gender(g: String) -> void:
	gender = g
	queue_redraw()

func _draw() -> void:
	var c = get_char_offset()
	var dc = get_draw_offset()
	var base_path = "res://assets/base_body_male.png" if gender == "male" else "res://assets/base_body.png"
	var base_tex = get_texture(base_path)
	if base_tex:
		draw_texture(base_tex, dc)

	var order = ["shoes", "bottom", "top"]
	for cat in order:
		if equipped.has(cat):
			var tex = get_texture(equipped[cat]["tex"])
			if tex:
				draw_texture(tex, dc)

	if equipped.has("hair"):
		var tex = get_texture(equipped["hair"]["tex"])
		if tex:
			draw_texture(tex, dc)

	if equipped.has("accessory"):
		var tex = get_texture(equipped["accessory"]["tex"])
		if tex:
			draw_texture(tex, dc)
