extends Control

signal item_equipped(category, item)
signal item_unequipped(category)

var equipped := {}
var textures := {}
var items := {}

var body_zones := {
	"accessory": Rect2(70, 2, 110, 35),
	"hair":      Rect2(73, 30, 104, 65),
	"top":       Rect2(70, 95, 110, 75),
	"bottom":    Rect2(95, 170, 60, 70),
	"shoes":     Rect2(95, 240, 60, 22),
}

var hovered_zone := ""

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
	return Vector2(-256, -256)

func get_zone_at(pos: Vector2) -> String:
	for zone in body_zones:
		if body_zones[zone].has_point(pos):
			return zone
	return ""

func _gui_input(event: InputEvent) -> void:
	if event is InputEventMouseMotion:
		var c = get_char_offset()
		var local = event.position - c
		var z = get_zone_at(local)
		if z != hovered_zone:
			hovered_zone = z
			var hint = {"accessory": "Accessory", "hair": "Hair", "top": "Top", "bottom": "Bottom", "shoes": "Shoes"}
			queue_redraw()

	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		var c = get_char_offset()
		var local = event.position - c
		var zone = get_zone_at(local)
		if zone:
			cycle_category(zone)
			accept_event()

func _draw() -> void:
	var c = get_char_offset()
	var dc = get_draw_offset()
	draw_rect(Rect2(c.x - 10, c.y - 10, 270, 320), Color(0.88, 0.85, 0.82), true)
	var base_tex = get_texture("res://assets/base_body.png")
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

	if hovered_zone and body_zones.has(hovered_zone):
		var zone = body_zones[hovered_zone]
		var zc = zone.get_center()
		draw_rect(Rect2(c.x + zone.position.x, c.y + zone.position.y, zone.size.x, zone.size.y), Color(1, 1, 1, 0.15), true)
		var label = {"accessory": "✧", "hair": "✧", "top": "✧", "bottom": "✧", "shoes": "✧"}
		var txt = label.get(hovered_zone, "")
		if txt:
			var font = ThemeDB.fallback_font
			var fs = ThemeDB.fallback_font_size
			draw_string(font, c + Vector2(zone.position.x + 4, zone.position.y + fs + 2), txt, HORIZONTAL_ALIGNMENT_LEFT, -1, fs, Color(1, 1, 1, 0.5))
