extends Control

const ITEMS_PER_PAGE := 9

@onready var char_display: Control = $CharacterDisplay
@onready var item_grid: GridContainer = $UI/Margin/VBox/ItemGrid
@onready var cat_buttons: HBoxContainer = $UI/Margin/VBox/CategoryButtons
@onready var remove_btn: Button = $UI/Margin/VBox/RemoveBtn
@onready var randomize_btn: Button = $RandomizeBtn
@onready var exit_btn: Button = $ExitBtn
@onready var category_label: Label = $UI/Margin/VBox/CategoryLabel
@onready var prev_btn: Button = $UI/Margin/VBox/PageNav/PrevBtn
@onready var next_btn: Button = $UI/Margin/VBox/PageNav/NextBtn
@onready var page_label: Label = $UI/Margin/VBox/PageNav/PageLabel
@onready var female_btn: Button = $UI/Margin/VBox/GenderButtons/FemaleBtn
@onready var male_btn: Button = $UI/Margin/VBox/GenderButtons/MaleBtn

var category_btns := {}
var current_category := ""
var current_page := 0

func _ready() -> void:
	build_category_buttons()
	select_category("top")
	remove_btn.pressed.connect(_on_remove_pressed)
	randomize_btn.pressed.connect(_on_randomize_pressed)
	exit_btn.pressed.connect(_on_exit_pressed)
	prev_btn.pressed.connect(_on_prev_page)
	next_btn.pressed.connect(_on_next_page)
	char_display.item_equipped.connect(_on_char_item_changed)
	char_display.item_unequipped.connect(_on_char_item_changed)
	char_display.gender_changed.connect(_on_gender_changed)
	female_btn.pressed.connect(_on_gender_pressed.bind("female"))
	male_btn.pressed.connect(_on_gender_pressed.bind("male"))
	_on_gender_pressed("female")

func _on_char_item_changed(_cat = null, _item = null) -> void:
	if current_category:
		refresh_items()

func _on_gender_pressed(g: String) -> void:
	char_display.set_gender(g)
	female_btn.button_pressed = g == "female"
	male_btn.button_pressed = g == "male"

func _on_gender_changed() -> void:
	current_page = 0
	if current_category:
		refresh_items()

func build_category_buttons() -> void:
	var cat_names = {
		"hair": "Hair", "top": "Top", "bottom": "Bottom",
		"shoes": "Shoes", "accessory": "Accessory",
	}
	for cat in char_display.get_categories():
		var btn = Button.new()
		btn.text = cat_names.get(cat, cat.capitalize())
		btn.custom_minimum_size = Vector2(0, 36)
		btn.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		btn.toggle_mode = true
		btn.pressed.connect(_on_category_pressed.bind(cat, btn))
		cat_buttons.add_child(btn)
		category_btns[cat] = btn

func _on_category_pressed(cat: String, btn: Button) -> void:
	for b in category_btns.values():
		b.button_pressed = false
	btn.button_pressed = true
	current_page = 0
	select_category(cat)

func select_category(cat: String) -> void:
	current_category = cat
	var cat_names = {
		"hair": "Hair", "top": "Top", "bottom": "Bottom",
		"shoes": "Shoes", "accessory": "Accessory",
	}
	category_label.text = cat_names.get(cat, cat.capitalize())
	refresh_items()

func _on_prev_page() -> void:
	if current_page > 0:
		current_page -= 1
		refresh_items()

func _on_next_page() -> void:
	var items = char_display.get_items(current_category)
	var max_page = max(0, ceil(items.size() / float(ITEMS_PER_PAGE)) - 1)
	if current_page < max_page:
		current_page += 1
		refresh_items()

func refresh_items() -> void:
	for child in item_grid.get_children():
		child.queue_free()

	var all_items = char_display.get_items(current_category)
	var equipped_item = char_display.get_equipped(current_category)
	var total = all_items.size()
	var max_page = max(0, ceil(total / float(ITEMS_PER_PAGE)) - 1)

	current_page = clampi(current_page, 0, max_page)

	var start = current_page * ITEMS_PER_PAGE
	var end = mini(start + ITEMS_PER_PAGE, total)
	var page_items = all_items.slice(start, end)

	for item in page_items:
		var btn = Button.new()
		btn.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		btn.size_flags_vertical = Control.SIZE_EXPAND_FILL

		var tex = load(item["tex"])
		if tex:
			btn.icon = tex
		btn.expand_icon = true

		if equipped_item and equipped_item["id"] == item["id"]:
			for s in ["normal", "hover", "pressed"]:
				btn.add_theme_stylebox_override(s, get_equipped_style())

		btn.pressed.connect(_on_item_pressed.bind(item))
		item_grid.add_child(btn)

	var empty = ITEMS_PER_PAGE - page_items.size()
	for i in empty:
		var spacer = Control.new()
		spacer.mouse_filter = Control.MOUSE_FILTER_IGNORE
		item_grid.add_child(spacer)

	prev_btn.disabled = current_page <= 0
	next_btn.disabled = current_page >= max_page
	page_label.text = str(current_page + 1) + " / " + str(max_page + 1) if total > 0 else ""

func get_equipped_style() -> StyleBoxFlat:
	var sb = StyleBoxFlat.new()
	sb.bg_color = Color8(100, 200, 100, 60)
	sb.border_color = Color8(80, 180, 80)
	sb.border_width_left = 2
	sb.border_width_right = 2
	sb.border_width_top = 2
	sb.border_width_bottom = 2
	sb.corner_radius_top_left = 4
	sb.corner_radius_top_right = 4
	sb.corner_radius_bottom_left = 4
	sb.corner_radius_bottom_right = 4
	return sb

func _on_item_pressed(item: Dictionary) -> void:
	var equipped_item = char_display.get_equipped(current_category)
	if equipped_item and equipped_item["id"] == item["id"]:
		char_display.unequip(current_category)
	else:
		char_display.equip(current_category, item)
	refresh_items()

func _on_randomize_pressed() -> void:
	var cats = char_display.get_categories()
	for cat in cats:
		var items = char_display.get_items(cat)
		if items.is_empty():
			continue
		var item = items[randi() % items.size()]
		char_display.equip(cat, item)
	refresh_items()

func _on_exit_pressed() -> void:
	get_tree().quit()

func _on_remove_pressed() -> void:
	if current_category:
		char_display.unequip(current_category)
		refresh_items()
