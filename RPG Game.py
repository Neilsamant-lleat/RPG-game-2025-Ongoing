import random
from time import sleep, time
import json

ALL_ENEMY_STATS = {
    'orc': {'hp': 150, 'ret_dmg_range': (0, 10), 'exp_reward': 20, 'intro': "\n--- Orc Battle! ---"},
    'goblin': {'hp': 50, 'ret_dmg_range': (0, 8), 'exp_reward': 10, 'intro': "\n--- Goblin Battle! ---"},
    'dragon': {'hp': 1000, 'ret_dmg_range': (20, 40), 'exp_reward': 200, 'intro': "\n--- Dragon Battle! ---"},
    'wyvern': {'hp': 200, 'ret_dmg_range': (6, 15), 'exp_reward': 30, 'special_effect': 'wyvern_venom_effect', 'intro': "\n--- Wyvern Battle! ---"},
    'wizard': {'hp': 175, 'ret_dmg_range': (10, 25), 'exp_reward': 50, 'intro': "I think it's time for you to destroy this guy."},
    'lobos_spirit': {'hp': 200, 'ret_dmg_range': (10, 25), 'exp_reward': 60, 'intro': "\n--- Lobos Spirit Battle! ---"},
    'hydra_knight': {'hp': 250, 'ret_dmg_range': (8, 18), 'exp_reward': 40, 'intro': "Hydra Knight engages!"},
    'zombie': {'hp': 80, 'ret_dmg_range': (5, 12), 'exp_reward': 15, 'intro': "\n--- Zombie Fight! ---"},
    'skeleton': {'hp': 90, 'ret_dmg_range': (6, 14), 'exp_reward': 18, 'intro': "\n--- Skeleton Fight! ---"},
    'skeletron': {'hp': 350, 'ret_dmg_range': (12, 28), 'exp_reward': 100, 'special_effect': 'skeletron_boss_effect', 'intro': "\n--- Skeletron Boss Fight! ---"},
    'eater_of_worlds': {'hp': 700, 'ret_dmg_range': (15, 30), 'exp_reward': 150, 'special_effect': 'eater_of_worlds_effect', 'intro': "\n--- Eater of Worlds Boss Fight! ---"},
    'steampunk_pirate': {'hp': 220, 'ret_dmg_range': (10, 20), 'exp_reward': 70, 'special_effect': 'steampunk_pirate_special', 'intro': "\n--- Steampunk Pirate Battle! ---"},
    'mettaton': {'hp': 600, 'ret_dmg_range': (15, 30), 'exp_reward': 120, 'special_effect': 'mettaton_special', 'intro': "\n--- It's Showtime! Mettaton Battle! ---"},
    'gash': {'hp': 300, 'ret_dmg_range': (15, 25), 'exp_reward': 80, 'special_effect': 'gash_special_effect', 'intro': "\n--- Phantom Shark Battle! ---"},
    'harpoon': {'hp': 250, 'ret_dmg_range': (12, 22), 'exp_reward': 75, 'special_effect': 'harpoon_special_effect', 'intro': "\n--- Deadly Siren Battle! ---"},
    'leat': {'hp': 400, 'ret_dmg_range': (15, 30), 'exp_reward': 150, 'intro': "\n--- BOSS FIGHT: LEAT, THE SILENT BLADE ---"},
    'elite_sentinel': {'hp': 200, 'ret_dmg_range': (10, 25), 'exp_reward': 60, 'intro': ""},
    'arcane_binder': {'hp': 180, 'ret_dmg_range': (12, 28), 'exp_reward': 55, 'intro': ""},
    'graystone': {'hp': 1800, 'ret_dmg_range': (25, 40), 'exp_reward': 250, 'intro': "\n--- BOSS FIGHT: GRAYSTONE, THE UNBREAKABLE MOUNTAIN ---"},
    'jade_golem': {'hp': 300, 'ret_dmg_range': (15, 25), 'exp_reward': 70, 'intro': "\n--- A Jade Golem lumbers towards you! ---"},
    'worshipper_acolyte': {'hp': 150, 'ret_dmg_range': (10, 20), 'exp_reward': 40, 'intro': "\n--- A Worshipper Acolyte confronts you! ---"},
    'angstrom_levy': {'hp': 2500, 'ret_dmg_range': (30, 45), 'exp_reward': 500, 'intro': "\n--- BOSS FIGHT: ANGSTROM LEVY, THE REALITY BENDER ---"},
    'magma_golem': {'hp': 350, 'ret_dmg_range': (20, 30), 'exp_reward': 80, 'intro': "\n--- A Magma Golem emerges from the lava! ---"},
    'ash_hound': {'hp': 180, 'ret_dmg_range': (15, 25), 'exp_reward': 50, 'intro': "\n--- An Ash Hound lunges from the smoke! ---"},
    'trench_kraken': {'hp': 400, 'ret_dmg_range': (18, 28), 'exp_reward': 90, 'intro': "\n--- A Trench Kraken erupts from the depths! ---"},
    'abyssal_shark': {'hp': 200, 'ret_dmg_range': (12, 22), 'exp_reward': 55, 'intro': "\n--- An Abyssal Shark speeds towards you! ---"},
    'cifer': {'hp': 3000, 'ret_dmg_range': (35, 50), 'exp_reward': 1000, 'intro': "\n--- BOSS FIGHT: CIFER, THE HOLLOW VESSEL ---"},
    'mistral': {'hp': 3500, 'ret_dmg_range': (40, 55), 'exp_reward': 1200, 'intro': "\n--- BOSS FIGHT: MISTRAL, THE COLD WIND ---"},
    'yakuza_enforcer': {'hp': 280, 'ret_dmg_range': (15, 28), 'exp_reward': 80, 'intro': "\n--- A Yakuza Enforcer blocks your path! ---"},
    'ronin': {'hp': 250, 'ret_dmg_range': (18, 32), 'exp_reward': 75, 'intro': "\n--- A masterless Ronin challenges you! ---"},
    'nightmare_fiend': {'hp': 320, 'ret_dmg_range': (20, 35), 'exp_reward': 90, 'intro': "\n--- A Nightmare Fiend materializes from the shadows! ---"},
    'weep_and_drown': {'hp': 4000, 'ret_dmg_range': (45, 60), 'exp_reward': 1500, 'intro': "\n--- BOSS FIGHT: WEEP AND DROWN, THE FIRST REGENT ---"},
    'roadside_bandit': {'hp': 200, 'ret_dmg_range': (10, 20), 'exp_reward': 50, 'intro': "\n--- Roadside Bandits ambush your truck! ---"},
    'battle_beast': {'hp': 1500, 'ret_dmg_range': (20, 35), 'exp_reward': 300, 'intro': "\n--- BOSS FIGHT: BATTLE BEAST ---"}
}

ALL_PLAYER_ATTACKS = {
    # --- Sword Attacks ---
    "flurry_strike": {"name": "Flurry Strike", "type": "attack", "desc": "A rapid series of slashes.", "dmg_range": (10, 25), "focus_cost": 0, "charge_gain": (10, 15)},
    "power_smash": {"name": "Power Smash", "type": "attack", "desc": "A slow but devastating overhead attack.", "dmg_range": (25, 40), "focus_cost": 25, "charge_gain": (15, 25)},
    "piercing_thrust": {"name": "Piercing Thrust", "type": "attack", "desc": "A precise thrust that ignores some enemy defenses.", "dmg_range": (20, 35), "focus_cost": 20, "charge_gain": (10, 20)},
    "whirlwind_slash": {"name": "Whirlwind Slash", "type": "attack", "desc": "Spinning attack hitting multiple times.", "dmg_range": (10, 20), "focus_cost": 0, "charge_gain": (10, 20), "hits": 2},
    "blade_dance": {"name": "Blade Dance", "type": "attack", "desc": "A quick three-hit combo.", "dmg_range": (8, 15), "focus_cost": 20, "charge_gain": (10, 15), "hits": 3},
    # --- Sword Specials ---
    "shadow_dash": {"name": "Shadow Dash", "type": "special", "desc": "Dash through the enemy, dealing damage and gaining focus.", "dmg_range": (15, 30), "focus_cost": 0, "charge_gain": (5, 10), "focus_gain": (10, 15)},
    "vampiric_slash": {"name": "Vampiric Slash", "type": "special", "desc": "Deals damage and heals for a portion of damage dealt.", "dmg_range": (15, 30), "focus_cost": 20, "charge_gain": (10, 15), "heal_percent_dmg": 0.5},
    "feint": {"name": "Feint", "type": "special", "desc": "Stun opponent next turn, make them take more damage.", "dmg_range": (0, 0), "focus_cost": 20, "charge_gain": (0, 0), "effect": "feint_stun"},
    "elegant_star": {"name": "Elegant Star", "type": "special", "desc": "Channel energy into a star, healing yourself.", "dmg_range": (0, 0), "focus_cost": 25, "charge_gain": (0, 0), "heal_amount": (30, 40)},
    "guard_break": {"name": "Guard Break", "type": "special", "desc": "A heavy blow that shatters defenses, making the enemy more vulnerable.", "dmg_range": (15, 25), "focus_cost": 30, "charge_gain": (5, 10), "effect": "guard_break"},
    # --- Lobos Sword Attacks ---
    "judgement_cut": {"name": "Judgement Cut", "type": "attack", "desc": "A swift and deadly cut.", "dmg_range": (35, 60), "focus_cost": 0, "charge_gain": (10, 20), "lobos_req": True},
    "true_strike": {"name": "True Strike", "type": "attack", "desc": "A precise strike, gaining focus.", "dmg_range": (20, 50), "focus_cost": 0, "charge_gain": (5, 10), "focus_gain": (5, 15), "lobos_req": True},
    "spectral_fang": {"name": "Spectral Fang", "type": "attack", "desc": "A rapid strike that may cause the enemy to bleed.", "dmg_range": (25, 45), "focus_cost": 25, "charge_gain": (5, 10), "effect": "spectral_bleed", "lobos_req": True},
    "phantom_rush": {"name": "Phantom Rush", "type": "attack", "desc": "A dashing attack that strikes twice.", "dmg_range": (18, 30), "focus_cost": 20, "charge_gain": (10, 15), "hits": 2, "lobos_req": True},
    "crescent_moon_slash": {"name": "Crescent Moon Slash", "type": "attack", "desc": "A wide, powerful slash imbued with spirit energy.", "dmg_range": (30, 55), "focus_cost": 30, "charge_gain": (15, 20), "lobos_req": True},
    # --- Lobos Sword Specials ---
    "rebound_barrage": {"name": "Rebound Barrage", "type": "special", "desc": "Deal damage over 3 turns.", "dmg_range": (40, 75), "focus_cost": 30, "charge_gain": (0, 0), "effect": "rebound_barrage", "lobos_req": True},
    "overdrive": {"name": "Overdrive", "type": "special", "desc": "Double damage next turn, but take 1.5x damage.", "dmg_range": (0, 0), "focus_cost": 70, "charge_gain": (0, 0), "effect": "overdrive_buff", "lobos_req": True},
    "lunar_phase": {"name": "Lunar Phase", "type": "special", "desc": "Dodge the next attack and recover focus.", "dmg_range": (0,0), "focus_cost": 0, "charge_gain": (0,0), "effect": "phase_dodge", "lobos_req": True},
    "spirit_siphon": {"name": "Spirit Siphon", "type": "special", "desc": "Strike the enemy's spirit, dealing damage and restoring your focus.", "dmg_range": (20, 30), "focus_cost": 10, "charge_gain": (5, 10), "focus_gain": (20, 30), "lobos_req": True},
    "wolfs_howl": {"name": "Wolf's Howl", "type": "special", "desc": "A spiritual howl that sharpens your senses, increasing critical hit chance.", "dmg_range": (0, 0), "focus_cost": 35, "charge_gain": (0, 0), "effect": "crit_buff", "lobos_req": True},
    # --- Beowulf Gauntlet Attacks ---
    "rising_dragon": {"name": "Rising Dragon", "type": "attack", "desc": "A powerful uppercut.", "dmg_range": (30, 50), "focus_cost": 0, "charge_gain": (10, 15), "beowulf_req": True},
    "straight_fist": {"name": "Straight Fist", "type": "attack", "desc": "A quick jab that builds combo potential.", "dmg_range": (15, 25), "focus_cost": 0, "charge_gain": (5, 10), "beowulf_req": True},
    "body_blow": {"name": "Body Blow", "type": "attack", "desc": "A solid punch to the torso that can weaken enemy attacks.", "dmg_range": (20, 35), "focus_cost": 15, "charge_gain": (8, 12), "effect": "weaken_enemy", "beowulf_req": True},
    "one_inch_punch": {"name": "One-Inch Punch", "type": "attack", "desc": "Unleash explosive power at close range.", "dmg_range": (50, 80), "focus_cost": 40, "charge_gain": (20, 30), "beowulf_req": True},
    "zodiac_dust": {"name": "Zodiac Dust", "type": "attack", "desc": "A flurry of shimmering, multi-hit blows.", "dmg_range": (12, 18), "focus_cost": 25, "charge_gain": (10, 20), "hits": 4, "beowulf_req": True},
    # --- Beowulf Gauntlet Specials ---
    "shockwave_palm": {"name": "Shockwave Palm", "type": "special", "desc": "A kinetic blast that stuns the enemy.", "dmg_range": (10, 20), "focus_cost": 25, "charge_gain": (5, 10), "effect": "stun_enemy", "beowulf_req": True},
    "pressure_point": {"name": "Pressure Point", "type": "special", "desc": "A precise strike that guarantees your next hit is critical.", "dmg_range": (5, 10), "focus_cost": 30, "charge_gain": (0, 0), "effect": "guaranteed_crit", "beowulf_req": True},
    "beast_within": {"name": "Beast Within", "type": "special", "desc": "Greatly boosts damage for 2 turns, but increases damage taken.", "dmg_range": (0, 0), "focus_cost": 35, "charge_gain": (0, 0), "effect": "beast_buff", "beowulf_req": True},
    "iron_will": {"name": "Iron Will", "type": "special", "desc": "Harden your resolve, reducing damage taken and healing slightly.", "dmg_range": (0, 0), "focus_cost": 0, "charge_gain": (0, 0), "effect": "iron_will_defense", "beowulf_req": True},
    "starfall": {"name": "Starfall", "type": "special", "desc": "Leap into the air and crash down, dealing AoE damage.", "dmg_range": (40, 60), "focus_cost": 30, "charge_gain": (15, 20), "beowulf_req": True},
    # --- Stance Specials ---
    "sunlight_yellow_overdrive": {"name": "Sunlight Yellow Overdrive", "type": "special", "desc": "Unleash a devastating punch charged with solar energy. (Only in Soleil Stance)", "dmg_range": (70, 110), "focus_cost": 60, "charge_gain": (20, 25), "stance_req": "soleil"},
    "lunar_horologium": {"name": "Lunar Horologium", "type": "special", "desc": "Reflect all incoming damage for 2 turns. (Only in Lune Stance)", "dmg_range": (0, 0), "focus_cost": 50, "charge_gain": (5, 10), "stance_req": "lune", "effect": "damage_reflect"},
    # --- Combo Finishers ---
    "combo_crescent_kick": {"name": "Crescent Kick", "type": "combo", "desc": "A powerful sweeping kick combo finisher.", "dmg_range": (40, 60), "focus_cost": 0, "charge_gain": (0,0), "beowulf_req": True},
    "combo_meteor_strike": {"name": "Meteor Strike", "type": "combo", "desc": "A heavy downward punch combo finisher.", "dmg_range": (80, 100), "focus_cost": 0, "charge_gain": (0,0), "beowulf_req": True},
    # --- Greaves of Sorrow Attacks ---
    "swift_kick": {"name": "Swift Kick", "type": "attack", "desc": "A quick and simple kick.", "dmg_range": (15, 30), "focus_cost": 0, "charge_gain": (10, 15), "boots_req": True},
    "axe_kick": {"name": "Axe Kick", "type": "attack", "desc": "A heavy downward kick that can break guards.", "dmg_range": (30, 45), "focus_cost": 25, "charge_gain": (15, 25), "effect": "guard_break", "boots_req": True},
    "spinning_heel_kick": {"name": "Spinning Heel Kick", "type": "attack", "desc": "A spinning kick that hits multiple times.", "dmg_range": (12, 22), "focus_cost": 0, "charge_gain": (10, 20), "hits": 2, "boots_req": True},
    "cyclone_kick": {"name": "Cyclone Kick", "type": "attack", "desc": "A rapid flurry of kicks.", "dmg_range": (10, 18), "focus_cost": 20, "charge_gain": (10, 15), "hits": 3, "boots_req": True},
    "stomp": {"name": "Stomp", "type": "attack", "desc": "A powerful stomp that shakes the ground.", "dmg_range": (25, 40), "focus_cost": 20, "charge_gain": (10, 20), "boots_req": True},
    # --- Greaves of Sorrow Specials ---
    "slide_tackle": {"name": "Slide Tackle", "type": "special", "desc": "Slide into the enemy, stunning them.", "dmg_range": (15, 30), "focus_cost": 20, "charge_gain": (5, 10), "effect": "stun_enemy", "boots_req": True},
    "backflip_kick": {"name": "Backflip Kick", "type": "special", "desc": "Dodge and counter with a powerful kick.", "dmg_range": (20, 35), "focus_cost": 25, "charge_gain": (10, 15), "effect": "phase_dodge", "boots_req": True},
    "mule_kick": {"name": "Mule Kick", "type": "special", "desc": "A powerful kick that sends the enemy reeling, reducing their damage.", "dmg_range": (25, 40), "focus_cost": 30, "charge_gain": (10, 20), "effect": "reduce_enemy_dmg", "boots_req": True},
    "gravity_stomp": {"name": "Gravity Stomp", "type": "special", "desc": "A stomp so powerful it makes the enemy heavier and slower.", "dmg_range": (20, 30), "focus_cost": 35, "charge_gain": (5, 10), "effect": "weaken_enemy", "boots_req": True},
    "comet_drop": {"name": "Comet Drop", "type": "special", "desc": "Leap high and come down with a devastating dive kick.", "dmg_range": (50, 70), "focus_cost": 40, "charge_gain": (20, 25), "boots_req": True},
    # --- Universal Specials ---
    "soul_reap": {"name": "Soul Reap", "type": "special", "desc": "Siphon life force from the enemy, dealing damage and healing yourself.", "dmg_range": (20, 30), "focus_cost": 30, "charge_gain": (5, 10), "heal_percent_dmg": 1.0},
    "tsunami_swiper": {"name": "Tsunami Swiper", "type": "special", "desc": "Summon a spectral wave, next attack applies bleed.", "dmg_range": (20, 50), "focus_cost": 35, "charge_gain": (10, 15), "effect": "bleed_next_turn"},
    "shockwave": {"name": "Shockwave", "type": "attack", "desc": "Slam the ground, damaging all enemies (AoE, for future use).", "dmg_range": (20, 30), "focus_cost": 20, "charge_gain": (10, 15)},
    "crippling_blow": {"name": "Crippling Blow", "type": "special", "desc": "Deals damage and reduces enemy's damage output next turn.", "dmg_range": (20, 35), "focus_cost": 25, "charge_gain": (10, 20), "effect": "reduce_enemy_dmg"},
    "healing_touch": {"name": "Healing Touch", "type": "special", "desc": "A minor heal for yourself.", "dmg_range": (0, 0), "focus_cost": 10, "charge_gain": (0, 0), "heal_amount": (10, 20)},
    "precision_strike": {"name": "Precision Strike", "type": "attack", "desc": "A highly accurate attack with a higher chance to crit.", "dmg_range": (20, 35), "focus_cost": 20, "charge_gain": (10, 15)},
    "burst_fire": {"name": "Burst Fire", "type": "attack", "desc": "Unleash a quick burst of elemental energy.", "dmg_range": (15, 25), "focus_cost": 15, "charge_gain": (10, 20)},
    "shield_bash": {"name": "Shield Bash", "type": "special", "desc": "Stun the enemy with a powerful shield strike.", "dmg_range": (10, 20), "focus_cost": 15, "charge_gain": (5, 10), "effect": "stun_enemy"},
}

BEOWULF_COMBOS = {
    ("straight_fist", "rising_dragon"): "combo_crescent_kick",
    ("body_blow", "body_blow", "one_inch_punch"): "combo_meteor_strike",
}

INITIAL_PLAYER_ATTACKS = [
    "flurry_strike", "power_smash", "piercing_thrust", "whirlwind_slash", "blade_dance"
]
INITIAL_PLAYER_SPECIALS = [
    "shadow_dash", "vampiric_slash", "feint", "elegant_star", "guard_break"
]

SAVABLE_GAME_STATE_KEYS = [
    'username', 'current_location', 'hp', 'charge', 'focus', 'max_focus', 'stance',
    'player_max_hp', 'player_base_dmg_min', 'player_base_dmg_max', 'level', 'exp',
    'default_sword', 'silver_sword', 'has_lobos_sword', 'lobos_power_unlocked',
    'has_beowulf_gauntlets', 'beowulf_style', 'gauntlet_favor',
    'has_greaves_of_sorrow', 'current_weapon',
    'ghost_form', 'has_firefly_armor', 'flaming_sword', 'lightning_sword',
    'arcane_sword', 'gale_sword', 'tsunami_swiper_unlocked',
    'gash_defeated', 'harpoon_defeated', 'wizard_defeated', 'battle_beast_defeated', 'leat_defeated',
    'graystone_defeated', 'angstrom_defeated', 'cifer_defeated', 'mistral_defeated', 'weep_and_drown_defeated',
    'player_attack_moveset', 'player_special_moveset',
    'diary_entries', 'last_moves_queue', 'player_clan', 'has_prism_armor',
]

game_state = {}

def get_new_game_state():
    return {
        'username': 'Player',
        'current_location': 'start_menu',
        'hp': 100,
        'charge': 0,
        'focus': 50,
        'max_focus': 100,
        'stance': "balanced",
        'crit_next_turn': False,
        'enemy_stunned': False,
        'enemy_damage_multiplier': 1.0,
        'rebound_barrage_active': False,
        'rebound_barrage_turns': 0,
        'rebound_barrage_remaining_dmg': 0,
        'overdrive_active': False,
        'overdrive_turns_left': 0,
        'bleed_next_turn': False,
        'phased_dodge_active': False,
        'beast_buff_active': False,
        'beast_buff_turns': 0,
        'lunar_horologium_active': False,
        'lunar_horologium_turns': 0,
        'wolfs_howl_active': False,
        'wolfs_howl_turns': 0,
        'default_sword': True,
        'silver_sword': False,
        'has_lobos_sword': False,
        'lobos_power_unlocked': False,
        'has_beowulf_gauntlets': False,
        'beowulf_style': None,
        'gauntlet_favor': None,
        'has_greaves_of_sorrow': False,
        'current_weapon': 'sword',
        'player_clan': None,
        'ghost_form': False,
        'has_firefly_armor': False,
        'has_prism_armor': False,
        'flaming_sword': False,
        'lightning_sword': False,
        'arcane_sword': False,
        'gale_sword': False,
        'tsunami_swiper_unlocked': False,
        'player_max_hp': 100,
        'player_base_dmg_min': 5,
        'player_base_dmg_max': 20,
        'level': 1,
        'exp': 0,
        'gash_defeated': False,
        'harpoon_defeated': False,
        'wizard_defeated': False,
        'battle_beast_defeated': False,
        'leat_defeated': False,
        'graystone_defeated': False,
        'angstrom_defeated': False,
        'cifer_defeated': False,
        'mistral_defeated': False,
        'weep_and_drown_defeated': False,
        'player_attack_moveset': list(INITIAL_PLAYER_ATTACKS),
        'player_special_moveset': list(INITIAL_PLAYER_SPECIALS),
        'diary_entries': [],
        'last_moves_queue': [],
    }

def get_player_input(prompt, valid_choices=None):
    while True:
        try:
            choice = int(input(prompt))
            if valid_choices is not None and choice not in valid_choices:
                print("Invalid choice. Please pick from the available options.")
                continue
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")
        print()

def get_save_filename(username):
    return f"rpg_save_{username.lower()}.txt"

def save_game():
    filename = get_save_filename(game_state['username'])
    savable_state = {key: game_state[key] for key in SAVABLE_GAME_STATE_KEYS if key in game_state}
    try:
        with open(filename, 'w') as f:
            # Convert the dictionary to a JSON string and write it to the .txt file
            f.write(json.dumps(savable_state, indent=4))
        print(f"Game saved to {filename}!")
    except Exception as e:
        print(f"Error saving game: {e}")
    sleep(1)

def load_game(username):
    global game_state
    filename = get_save_filename(username)
    try:
        with open(filename, 'r') as f:
            # Read the JSON string from the .txt file and parse it
            loaded_state = json.loads(f.read())
        
        default_game_state = get_new_game_state()
        game_state = default_game_state

        for key in SAVABLE_GAME_STATE_KEYS:
            game_state[key] = loaded_state.get(key, default_game_state.get(key))

        game_state['username'] = loaded_state.get('username', username)
        
        print(f"Game loaded for user '{game_state['username']}' from {filename}!")
        sleep(1)
        return True
    except FileNotFoundError:
        print(f"No save game found for user '{username}'.")
        sleep(1)
        return False
    except json.JSONDecodeError:
        print(f"Error reading save file for '{username}'. The file may be corrupted or in an old format.")
        sleep(1)
        return False
    except Exception as e:
        print(f"An unexpected error occurred while loading the game: {e}")
        sleep(1)
        return False

def award_exp(exp_amount):
    game_state['exp'] += exp_amount
    print(f"You gained {exp_amount} experience points!")
    sleep(1)
    while game_state['exp'] >= game_state['level'] * 100:
        game_state['exp'] -= game_state['level'] * 100
        game_state['level'] += 1
        game_state['player_max_hp'] += 10
        game_state['player_base_dmg_min'] += 3
        game_state['player_base_dmg_max'] += 5
        game_state['max_focus'] += 5
        game_state['hp'] = game_state['player_max_hp']
        game_state['focus'] = game_state['max_focus']
        print(f"\n--- LEVEL UP! You reached Level {game_state['level']}! ---")
        print(f"Your max HP increased to {game_state['player_max_hp']}!")
        print(f"Your base damage range is now {game_state['player_base_dmg_min']}-{game_state['player_base_dmg_max']}!")
        print(f"Your max Focus increased to {game_state['max_focus']}!")
        sleep(2)

def apply_stance_modifiers(dmg, ret_dmg, current_stance):
    # Base Stances
    if current_stance == "offensive" or current_stance == "soleil":
        dmg_mult = 1.3 if current_stance == "soleil" else 1.2
        ret_dmg_mult = 1.3 if current_stance == "soleil" else 1.2
        dmg = int(dmg * dmg_mult)
        ret_dmg = int(ret_dmg * ret_dmg_mult)
        print(f"Your {current_stance.capitalize()} Stance channels your aggression, dealing more damage but leaving you open!")
    elif current_stance == "defensive" or current_stance == "lune":
        dmg_mult = 0.7 if current_stance == "lune" else 0.8
        ret_dmg_mult = 0.7 if current_stance == "lune" else 0.8
        dmg = int(dmg * dmg_mult)
        ret_dmg = int(ret_dmg * ret_dmg_mult)
        print(f"Your {current_stance.capitalize()} Stance hardens your resolve, taking less damage but reducing your attack power!")
    else:
        print("You maintain a Balanced Stance, ready for anything.")

    # Ghost Form Modifiers
    if game_state.get('ghost_form', False):
        if current_stance in ["offensive", "soleil"]:
            dmg = int(dmg * 1.1)
            ret_dmg = int(ret_dmg * 1.1)
            print("The ghost presence enhances your offensive might but exposes you further!")
        elif current_stance in ["defensive", "lune"]:
            dmg = int(dmg * 0.9)
            ret_dmg = int(ret_dmg * 0.9)
            print("The ghost presence solidifies your defense but dulls your attacks!")
        elif current_stance == "balanced":
            dmg = int(dmg * 1.05)
            ret_dmg = int(ret_dmg * 1.05)
            print("The ghost presence subtly shifts your balance.")

    # Gale Sword Modifiers
    if game_state.get('gale_sword', False):
        dmg = int(dmg * 0.95)
        ret_dmg = int(ret_dmg * 0.9)
        print("Your Gale Sword subtly shifts the battlefield to your advantage!")

    # Prism Armor Modifier
    if game_state.get('has_prism_armor', False):
        ret_dmg = int(ret_dmg * 0.9) # 10% damage reduction
        print("Your Prism Armor glows, deflecting a portion of the incoming damage!")

    # Lune Favor Modifier
    if game_state.get('gauntlet_favor') == 'lune':
        ret_dmg = int(ret_dmg * 0.95) # 5% damage reduction

    return dmg, ret_dmg

def check_for_beowulf_combo(enemy_name, enemy_hp):
    queue_tuple = tuple(game_state['last_moves_queue'])
    combo_move = None

    for combo, move in BEOWULF_COMBOS.items():
        combo_len = len(combo)
        if len(queue_tuple) >= combo_len and queue_tuple[-combo_len:] == combo:
            combo_move = move
            break

    if combo_move:
        print("\n--- COMBO! ---")
        sleep(1)
        enemy_hp, _ = attack_enemy(enemy_name, enemy_hp, combo_move, (0, 0))
        game_state['last_moves_queue'].clear()
    
    return enemy_hp

def attack_enemy(enemy_name, enemy_hp, attack_name, enemy_ret_range):
    attack_data = ALL_PLAYER_ATTACKS.get(attack_name)
    if not attack_data:
        print(f"Error: Attack '{attack_name}' not found.")
        return enemy_hp, False

    # Check Requirements
    if attack_data.get("lobos_req") and not game_state.get('has_lobos_sword', False):
        print(f"You need the Lobos sword to use {attack_data['name']}!")
        return enemy_hp, False
    if attack_data.get("beowulf_req") and (not game_state.get('has_beowulf_gauntlets', False) or game_state.get('current_weapon') != 'gauntlets'):
        print(f"You must have the Beowulf gauntlets equipped to use {attack_data['name']}!")
        return enemy_hp, False
    if attack_data.get("boots_req") and (not game_state.get('has_greaves_of_sorrow', False) or game_state.get('current_weapon') != 'boots'):
        print(f"You must have the Greaves of Sorrow equipped to use {attack_data['name']}!")
        return enemy_hp, False
    required_stance = attack_data.get("stance_req")
    if required_stance and game_state.get('stance') != required_stance:
        print(f"You must be in {required_stance.capitalize()} Stance to use {attack_data['name']}!")
        return enemy_hp, False
    
    # Check Focus Cost
    cost = attack_data.get("focus_cost", 0)
    if game_state['focus'] < cost:
        print(f"Not enough Focus for {attack_data['name']}! (Requires {cost} Focus)")
        return enemy_hp, False
    game_state['focus'] -= cost
    game_state['focus'] = max(0, game_state['focus'])

    # Calculate Damage
    base_dmg = random.randint(attack_data['dmg_range'][0], attack_data['dmg_range'][1])
    scaled_dmg_min = game_state['player_base_dmg_min'] + attack_data['dmg_range'][0]
    scaled_dmg_max = game_state['player_base_dmg_max'] + attack_data['dmg_range'][1]
    base_dmg = random.randint(scaled_dmg_min, scaled_dmg_max)
    base_ret_dmg = random.randint(enemy_ret_range[0], enemy_ret_range[1])
    
    actual_dmg, actual_ret_dmg = apply_stance_modifiers(base_dmg, base_ret_dmg, game_state['stance'])

    # Special Item/Buff Damage Modifiers
    if game_state.get('arcane_sword', False):
        arcane_bonus = random.randint(5, 15)
        actual_dmg += arcane_bonus
        print(f"Your Arcane Sword pulses with energy, adding {arcane_bonus} bonus damage!")
    if game_state.get('overdrive_active', False):
        actual_dmg = int(actual_dmg * 2)
        print("OVERDRIVE: Your attack is empowered!")
    if game_state.get('beast_buff_active', False):
        actual_dmg = int(actual_dmg * 1.5)
        print("BEAST WITHIN: Your attack is ferocious!")
    if game_state.get('gauntlet_favor') == 'soleil':
        actual_dmg = int(actual_dmg * 1.05) # 5% damage boost

    actual_dmg = int(actual_dmg * game_state['enemy_damage_multiplier'])
    
    # Handle Multi-hit attacks
    total_dmg_dealt = 0
    if "hits" in attack_data:
        num_hits = attack_data["hits"]
        for i in range(num_hits):
            hit_dmg = random.randint(attack_data['dmg_range'][0], attack_data['dmg_range'][1])
            total_dmg_dealt += hit_dmg
        actual_dmg += total_dmg_dealt # Add to scaled damage
        print(f"You unleash {attack_data['name']}, landing {num_hits} hits for a total of {actual_dmg} damage!")
    else:
        if attack_data.get("type") != "combo":
            print(f"You use {attack_data['name']} on the {enemy_name} for {actual_dmg} damage.")
        else:
            print(f"Your combo flows into {attack_data['name']}, striking the {enemy_name} for {actual_dmg} damage!")

    # Clan Buffs (Dojima)
    if game_state.get('player_clan') == 'dojima' and random.random() < 0.15: # 15% chance
        dojima_bonus_dmg = int(actual_dmg * 0.5)
        actual_dmg += dojima_bonus_dmg
        print(f"The Mark of the Dragon flares! You deal an extra {dojima_bonus_dmg} damage!")

    # Critical Hit Calculation
    crit_chance = 0.05 
    if game_state.get('wolfs_howl_active', False):
        crit_chance += 0.25 
    is_critical = False
    if game_state['crit_next_turn']:
        is_critical = True
        print("Your parry created an opening!")
        game_state['crit_next_turn'] = False
    elif random.random() < crit_chance:
        is_critical = True
        print("You strike a weak point!")
    if is_critical:
        crit_mult = random.uniform(1.5, 2.0)
        actual_dmg = int(actual_dmg * crit_mult)
        print(f"CRITICAL HIT! Damage multiplied to {actual_dmg}!")
        
    enemy_hp -= actual_dmg
    sleep(2)
    print(f"It now has {enemy_hp} health.")
    print()
    sleep(2)

    # Post-Attack Logic
    if attack_data.get("beowulf_req") and attack_data.get("type") == "attack":
        game_state['last_moves_queue'].append(attack_name)
        if len(game_state['last_moves_queue']) > 3:
            game_state['last_moves_queue'].pop(0)
        enemy_hp = check_for_beowulf_combo(enemy_name, enemy_hp)

    # Handle Effects
    effect = attack_data.get("effect")
    if effect:
        if effect == "bleed_next_turn":
            game_state['bleed_next_turn'] = True
            print("You gain a 'Shark Charge' for your next attack!")
        elif effect == "rebound_barrage":
            total_barrage_dmg = random.randint(attack_data['dmg_range'][0], attack_data['dmg_range'][1])
            game_state['rebound_barrage_active'] = True
            game_state['rebound_barrage_turns'] = 3
            game_state['rebound_barrage_remaining_dmg'] = total_barrage_dmg
            print(f"You unleash a powerful Rebound Barrage! It will deal {total_barrage_dmg} damage over 3 turns.")
        elif effect == "overdrive_buff":
            game_state['overdrive_active'] = True
            game_state['overdrive_turns_left'] = 1
            print("You activate Overdrive! Your body surges with power. Your next attack will deal double damage, but you will take 1.5x damage!")
        elif effect == "feint_stun":
            game_state['enemy_stunned'] = True
            game_state['crit_next_turn'] = False
            game_state['enemy_damage_multiplier'] = 1.25
            print(f"You execute a clever Feint, faking an attack that leaves the {enemy_name} stunned and vulnerable!")
        elif effect == "stun_enemy":
            game_state['enemy_stunned'] = True
            print(f"Your {attack_data['name']} stuns the {enemy_name}!")
        elif effect == "reduce_enemy_dmg":
            game_state['enemy_damage_multiplier'] = 0.75
            print(f"Your {attack_data['name']} leaves the {enemy_name} vulnerable!")
        elif effect == "phase_dodge":
            game_state['phased_dodge_active'] = True
            print("You phase into a lunar stance, prepared to dodge the next blow!")
        elif effect == "beast_buff":
            game_state['beast_buff_active'] = True
            game_state['beast_buff_turns'] = 2
            print("You roar, unleashing the Beast Within! Your damage is increased, but so is the damage you take!")
        elif effect == "damage_reflect":
            if game_state.get('lunar_horologium_active', False):
                print("Lunar Horologium is already active!")
                return enemy_hp, False
            game_state['lunar_horologium_active'] = True
            game_state['lunar_horologium_turns'] = 2
            print("You trace a silver circle of power. For the next 2 turns, all damage will be reflected!")
        elif effect == "crit_buff":
            game_state['wolfs_howl_active'] = True
            game_state['wolfs_howl_turns'] = 3
            print("A spiritual howl echoes, sharpening your instincts! Your critical hit chance is increased!")
        return enemy_hp, True

    # Healing
    if "heal_percent_dmg" in attack_data:
        heal = int(actual_dmg * attack_data["heal_percent_dmg"])
        game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + heal)
        print(f"You heal for {heal} HP! Your health is now {game_state['hp']}.")
    elif "heal_amount" in attack_data:
        heal = random.randint(attack_data['heal_amount'][0], attack_data['heal_amount'][1])
        game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + heal)
        print(f"You heal for {heal} HP! Your health is now {game_state['hp']}.")

    # Special follow-up effects
    if game_state.get('bleed_next_turn', False):
        bleed_dmg = random.randint(10, 25)
        enemy_hp -= bleed_dmg
        print(f"The 'Shark Charge' from your previous move tears open a wound! The {enemy_name} bleeds for an extra {bleed_dmg} damage! It now has {enemy_hp} health.")
        game_state['bleed_next_turn'] = False
        sleep(2)
    
    # Enemy Retaliation
    if game_state.get('phased_dodge_active', False):
        print(f"You effortlessly dodge the {enemy_name}'s counter attack!")
        game_state['phased_dodge_active'] = False
        return enemy_hp, True
    if game_state.get('lunar_horologium_active', False):
        print(f"The {enemy_name} prepares to counter, but your Lunar Horologium is active!")
        return enemy_hp, True

    if game_state.get('overdrive_active', False):
        game_state['hp'] -= int(actual_ret_dmg * 1.5)
        print("OVERDRIVE: The power leaves you exposed, and you take increased retaliation damage!")
        game_state['overdrive_turns_left'] -= 1
        if game_state['overdrive_turns_left'] <= 0:
            game_state['overdrive_active'] = False
            print("Overdrive wears off.")
    else:
        game_state['hp'] -= actual_ret_dmg

    # Gain Charge and Focus
    charge_gain = random.randint(attack_data['charge_gain'][0], attack_data['charge_gain'][1])
    game_state['charge'] = min(100, game_state['charge'] + charge_gain)
    
    focus_gain_range = attack_data.get("focus_gain", (0,0))
    focus_gain = random.randint(focus_gain_range[0], focus_gain_range[1])
    if game_state.get('player_clan') == 'ginryu':
        focus_gain = int(focus_gain * 1.25) # 25% more focus gain
    if focus_gain > 0:
        game_state['focus'] = min(game_state['max_focus'], game_state['focus'] + focus_gain)
    
    # Print retaliation and status
    if attack_data.get("type") != "combo":
        print(f"The {enemy_name} counters with a savage blow for {actual_ret_dmg} damage. Your health is now {game_state['hp']}")
        print(f"You gained {charge_gain} ultimate charge. Total charge: {game_state['charge']}.")
        print(f"Current Focus: {game_state['focus']}.")
        print()
    
    # Elemental Sword Effects
    if game_state.get('flaming_sword', False) and enemy_hp > 0:
        burn_dmg = random.randint(3, 8)
        enemy_hp -= burn_dmg
        print(f"The {enemy_name} is burned by your Flaming Sword, taking {burn_dmg} additional damage! It now has {enemy_hp} health.")
    if game_state.get('lightning_sword', False) and enemy_hp > 0 and random.random() < 0.25:
        game_state['enemy_stunned'] = True
        print(f"Your Lightning Sword crackles, sending a jolt through the {enemy_name} and stunning it!")
        
    return enemy_hp, True

def defend(enemy_name, def_type, ret_range, charge_gain_range=(5, 20)):
    base_ret_dmg = random.randint(ret_range[0], ret_range[1])
    _, actual_ret = apply_stance_modifiers(0, base_ret_dmg, current_stance=game_state['stance'])
    action_taken = True

    # Buffs that increase damage taken
    if game_state.get('overdrive_active', False):
        actual_ret = int(actual_ret * 1.5)
        print("OVERDRIVE: The raw power coursing through you makes defense difficult! You take increased damage!")
        game_state['overdrive_turns_left'] -= 1
        if game_state['overdrive_turns_left'] <= 0:
            game_state['overdrive_active'] = False
            print("Overdrive wears off.")
    if game_state.get('beast_buff_active', False):
        actual_ret = int(actual_ret * 1.5)
        print("BEAST WITHIN: Your heightened aggression makes you reckless! You take increased damage!")

    if def_type == "parry":
        cost = 20
        if game_state['focus'] < cost:
            print("Not enough Focus for Parry! (Requires 20 Focus)")
            action_taken = False
        else:
            game_state['focus'] -= cost
            chance = random.randint(1, 4)
            if chance == 1:
                print(f"With a sharp ring of steel, you perfectly parried the {enemy_name}'s attack!")
                print("The enemy is momentarily off balance, creating an opening! Your next attack will be a critical hit!")
                game_state['crit_next_turn'] = True
                game_state['enemy_stunned'] = True
                sleep(2)
            else:
                game_state['hp'] -= int(actual_ret * 1.5)
                print(f"You failed the parry and the blow knocked you off-balance! The {enemy_name} hit you for {int(actual_ret * 1.5)} damage.")
                print(f"Your health is now {game_state['hp']}")
                game_state['crit_next_turn'] = False
                game_state['enemy_stunned'] = False
            print(f"Current Focus: {game_state['focus']}.")
            print()
    elif def_type == "focus_charge":
        dmg_taken = random.randint(10, 20)
        game_state['hp'] -= dmg_taken
        gain = random.randint(30, 60)
        if game_state.get('player_clan') == 'ginryu':
            gain = int(gain * 1.25)
        game_state['focus'] = min(game_state['max_focus'], game_state['focus'] + gain)
        sleep(2)
        print(f"You brace for the hit, channeling your pain into pure focus! You took {dmg_taken} damage but gained {gain} Focus.")
        print(f"Your health is now {game_state['hp']}. Current Focus: {game_state['focus']}.")
        print()
        game_state['crit_next_turn'] = False
        game_state['enemy_stunned'] = False
    else:
        print("Invalid defense type.")
        action_taken = False
        
    return action_taken

def use_ult(enemy_name, enemy_hp):
    action_taken = False
    if game_state['charge'] < 100:
        print("You don't have enough charge to use your Ultimate.")
        print()
        return enemy_hp, action_taken

    if game_state.get('has_beowulf_gauntlets', False):
        return beowulf_ult(enemy_name, enemy_hp)
    elif game_state.get('has_lobos_sword', False) and game_state.get('lobos_power_unlocked', False):
        enemy_hp, _, _, action_taken = lobos_true_power_ult(enemy_name, enemy_hp)
        return enemy_hp, action_taken
    else:
        ult_dmg = random.randint(90, 130) + game_state['player_base_dmg_max']
        enemy_hp -= ult_dmg
        print(f"You unleash a whirlwind of attacks! Your Ultimate 'Slash Frenzy' tears into the {enemy_name} for {ult_dmg} damage!")
        print(f"The {enemy_name} now has {enemy_hp} health.")
        game_state['charge'] = 0
        print()
        action_taken = True
        
    return enemy_hp, action_taken

def check_ult_charge():
    print(f"Your ultimate charge is: {game_state['charge']}")
    print()

def check_focus_amount():
    print(f"Your Focus is: {game_state['focus']}/{game_state['max_focus']}")
    print()

def change_player_stance():
    print("Changing stance...")
    sleep(1)
    if game_state.get('has_beowulf_gauntlets'):
        stance_choice = get_player_input("""Choose your new stance:
1. Soleil (Deal +30% damage, Take +30% damage, Unlocks 'Sunlight Yellow Overdrive')
2. Lune (Deal -30% damage, Take -30% damage, Unlocks 'Lunar Horologium')
3. Balanced (No modifiers)
Choice: """, valid_choices=[1, 2, 3])
        print()
        if stance_choice == 1:
            print("You channel the radiant power of Soleil. Feel the burn!")
            game_state['stance'] = "soleil"
        elif stance_choice == 2:
            print("You embrace the calm reflection of Lune. Patience and precision.")
            game_state['stance'] = "lune"
        elif stance_choice == 3:
            print("You return to a Balanced Stance.")
            game_state['stance'] = "balanced"
    else:
        stance_choice = get_player_input("""Choose your new stance:
1. Offensive (Deal +20% damage, Take +20% damage)
2. Defensive (Deal -20% damage, Take -20% damage)
3. Balanced (No modifiers)
Choice: """, valid_choices=[1, 2, 3])
        print()
        if stance_choice == 1:
            print("You switch to an Offensive Stance. Be aggressive!")
            game_state['stance'] = "offensive"
        elif stance_choice == 2:
            print("You switch to a Defensive Stance. Brace for impact!")
            game_state['stance'] = "defensive"
        elif stance_choice == 3:
            print("You return to a Balanced Stance.")
            game_state['stance'] = "balanced"

def lobos_true_power_ult(enemy_name, enemy_hp):
    sleep(1)
    if game_state['charge'] < 100:
        print("Not enough ultimate charge to awaken Lobos' true power!")
        return enemy_hp, False, False, False
        
    choice = get_player_input("""What will you do with awakened Lobos?
                      1. Lobos Beam (Deals 30-80 damage, ranged attack)
                      2. Fury Combo (Deals 20-70 damage and heals you for 10-30 health, melee burst)
                      3. Metralleta (Deals 10-40 damage multiple times, total 30-120 damage, chance to miss)
                      Choice:""", valid_choices=[1, 2, 3])
    print()
    
    game_state['charge'] = 0
    action_taken = True
    
    if choice == 1:
        lob_dmg = random.randint(30, 80) + game_state['player_base_dmg_max']
        lob_dmg = int(lob_dmg * game_state['enemy_damage_multiplier'])
        enemy_hp -= lob_dmg
        sleep(2)
        print(f"You unleash a searing beam of pure energy from your sword at {enemy_name}! It dealt {int(lob_dmg)} damage. {enemy_name} is now at {enemy_hp} health.")
    elif choice == 2:
        fury_dmg = random.randint(20, 70) + game_state['player_base_dmg_max']
        fury_dmg = int(fury_dmg * game_state['enemy_damage_multiplier'])
        heal_amt = random.randint(10, 30)
        enemy_hp -= fury_dmg
        game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + heal_amt)
        sleep(2)
        print(f"You use Fury Combo on {enemy_name}, a blinding flurry of strikes that deals {int(fury_dmg)} damage!")
        print(f"The energy flowing back into you heals for {heal_amt} health. Your health is now {game_state['hp']}")
        print(f"The {enemy_name} is now at {enemy_hp} health.")
    elif choice == 3:
        total_met_dmg = 0
        hits = 0
        for _ in range(random.randint(3, 5)):
            if random.random() < 0.8:
                hit_dmg = random.randint(10, 40) + game_state['player_base_dmg_max'] // 2
                hit_dmg = int(hit_dmg * game_state['enemy_damage_multiplier'])
                total_met_dmg += hit_dmg
                hits += 1
            else:
                print("One of your Metralleta slashes went wide!")
            sleep(0.5)
        enemy_hp -= total_met_dmg
        sleep(2)
        print(f"You unleash Metralleta on {enemy_name}, landing {hits} spectral slashes for a total of {int(total_met_dmg)} damage!")
        print(f"The {enemy_name} is now at {enemy_hp} health.")
    else:
        print("Invalid choice. You hesitated and wasted your ultimate opportunity!")
        action_taken = False
        return enemy_hp, False, False, False
        
    game_state['crit_next_turn'] = False
    game_state['enemy_stunned'] = False
    game_state['enemy_damage_multiplier'] = 1.0
    print()
    return enemy_hp, game_state['crit_next_turn'], game_state['enemy_stunned'], action_taken

def beowulf_ult(enemy_name, enemy_hp):
    sleep(1)
    if game_state['charge'] < 100:
        print("Not enough ultimate charge for Final Heaven!")
        return enemy_hp, False
        
    choice = get_player_input("""Unleash the power of the beast?
                      1. Final Heaven (Single massive damage punch)
                      2. Rising Phoenix (Deal damage and revive with 25% HP if knocked out this turn)
                      3. Dragon's Roar (Stun all enemies and grant yourself a damage buff)
                      Choice: """, valid_choices=[1, 2, 3])
    print()
    
    game_state['charge'] = 0
    action_taken = True
    
    if choice == 1:
        ult_dmg = random.randint(150, 250) + game_state['player_base_dmg_max']
        ult_dmg = int(ult_dmg * game_state['enemy_damage_multiplier'])
        enemy_hp -= ult_dmg
        sleep(2)
        print(f"You channel all your power into a single fist and unleash FINAL HEAVEN! The impact is deafening, dealing {ult_dmg} damage!")
        print(f"{enemy_name} is now at {enemy_hp} health.")
    elif choice == 2:
        ult_dmg = random.randint(80, 120) + game_state['player_base_dmg_max']
        ult_dmg = int(ult_dmg * game_state['enemy_damage_multiplier'])
        enemy_hp -= ult_dmg
        sleep(2)
        print(f"You soar upwards wreathed in spiritual energy, crashing down on the enemy like a RISING PHOENIX, dealing {ult_dmg} damage!")
        print("The embers of the phoenix will revive you if you fall this turn.")
    elif choice == 3:
        print("You unleash a mighty DRAGON'S ROAR! The concussive force stuns the enemy and fills you with power!")
        game_state['enemy_stunned'] = True
        game_state['beast_buff_active'] = True
        game_state['beast_buff_turns'] = 2
        print("You are now under the effects of Beast Within!")
        
    return enemy_hp, action_taken

# --- Special Enemy Effects ---
def wyvern_venom_effect(enemy_name):
    game_state['hp'] -= 3
    print(f"The {enemy_name}'s claws leave a venomous residue. You take 3 poison damage. Your health is now {game_state['hp']}")

def skeletron_boss_effect(enemy_name):
    damage_dealt = 5
    game_state['hp'] -= damage_dealt
    print(f"Skeletron unleashes a rattling bone curse! You take {damage_dealt} damage. Your health is now {game_state['hp']}")

def eater_of_worlds_effect(enemy_name):
    damage_dealt = random.randint(8, 20)
    game_state['hp'] -= damage_dealt
    print(f"The {enemy_name} burrows and erupts from beneath you, dealing {damage_dealt} damage! Your health is now {game_state['hp']}")

def steampunk_pirate_special(enemy_name):
    if random.random() < 0.3:
        print(f"The {enemy_name} fires a grappling hook!")
        sleep(1)
        if random.random() < 0.5:
            print("The hook snags you, pulling you off balance! You are stunned!")
            game_state['enemy_stunned'] = True
            extra_dmg = random.randint(5, 10)
            game_state['hp'] -= extra_dmg
            print(f"You take an extra {extra_dmg} damage while trying to get free!")
        else:
            print("You manage to dodge the hook just in time!")

def mettaton_special(enemy_name):
    action = random.choice(["pose", "legs", "bombs"])
    if action == "pose":
        print("Mettaton strikes a dramatic pose! The ratings are going through the roof! (Mettaton's next attack will be stronger)")
        return "empower"
    elif action == "legs":
        leg_dmg = random.randint(15, 25)
        print(f"Mettaton's legs go wild, kicking with incredible speed! You take {leg_dmg} damage!")
        game_state['hp'] -= leg_dmg
    elif action == "bombs":
        print("Mettaton drops a series of mini-bombs! You have to dodge!")
        if random.random() < 0.6:
            print("You weave through the explosions masterfully!")
        else:
            bomb_dmg = random.randint(10, 20)
            print(f"You get clipped by an explosion for {bomb_dmg} damage!")
            game_state['hp'] -= bomb_dmg
    return None

def gash_special_effect(enemy_name):
    if random.random() < 0.3:
        print("Gash thrashes wildly, inflicting a Phantom Wound!")
        bleed_dmg = random.randint(5, 10)
        game_state['hp'] -= bleed_dmg
        print(f"The wound continues to bleed, dealing {bleed_dmg} damage. Your health is now {game_state['hp']}")

def harpoon_special_effect(enemy_name):
    if random.random() < 0.35:
        print("Harpoon sings a mesmerizing, deadly tune!")
        if random.random() < 0.5:
            print("You are charmed by the siren's song and hesitate!")
            charm_dmg = random.randint(10, 20)
            game_state['hp'] -= charm_dmg
            print(f"You drop your guard for a moment, taking {charm_dmg} damage!")
        else:
            print("You resist the enchanting melody!")

def battle_sequence(enemy_type, win_hp_bonus=0, death_hp_reset=None, intro_text=""):
    enemy_data = ALL_ENEMY_STATS.get(enemy_type)
    if not enemy_data:
        print(f"Error: Enemy type '{enemy_type}' not found in ALL_ENEMY_STATS.")
        return "error"
    enemy_name = enemy_type.replace('_', ' ').title()
    initial_enemy_hp = enemy_data['hp']
    default_ret_range = enemy_data['ret_dmg_range']
    special_enemy_effect_func = globals().get(enemy_data.get('special_effect'))
    enemy_hp = initial_enemy_hp
    if death_hp_reset is not None:
        game_state['hp'] = death_hp_reset
    else:
        game_state['hp'] = game_state['player_max_hp']

    # Clan Buff (Tojo)
    start_charge = 25 if game_state.get('player_clan') == 'tojo' else 0
    game_state['charge'] = start_charge
    
    game_state['focus'] = game_state['max_focus'] // 2
    game_state['stance'] = "balanced"
    game_state['crit_next_turn'] = False
    game_state['enemy_stunned'] = False
    game_state['enemy_damage_multiplier'] = 1.0
    game_state['overdrive_active'] = False
    game_state['overdrive_turns_left'] = 0
    game_state['rebound_barrage_active'] = False
    game_state['rebound_barrage_turns'] = 0
    game_state['rebound_barrage_remaining_dmg'] = 0
    game_state['bleed_next_turn'] = False
    game_state['last_moves_queue'].clear()
    mettaton_empowered = False
    print(intro_text if intro_text else enemy_data.get('intro', f"\n--- {enemy_name} Battle! ---"))
    sleep(1)

    while True:
        sleep(1)
        if game_state['lunar_horologium_active']:
            game_state['lunar_horologium_turns'] -= 1
            print(f"Lunar Horologium has {game_state['lunar_horologium_turns']} turns remaining.")
            if game_state['lunar_horologium_turns'] <= 0:
                game_state['lunar_horologium_active'] = False
                print("Your damage reflection fades.")
        if game_state['wolfs_howl_active']:
            game_state['wolfs_howl_turns'] -= 1
            print(f"Wolf's Howl has {game_state['wolfs_howl_turns']} turns remaining.")
            if game_state['wolfs_howl_turns'] <= 0:
                game_state['wolfs_howl_active'] = False
                print("Your heightened senses return to normal.")

        if game_state['hp'] <= 0:
            print(f"\nYou are knocked out by the {enemy_name}. You are lucky that I haven't decided to restart you back to the beginning, but I will also heal the {enemy_name}. GET BACK IN THE FIGHT!")
            print()
            game_state['hp'] = game_state['player_max_hp']
            enemy_hp = initial_enemy_hp
            game_state['charge'] = start_charge
            game_state['focus'] = game_state['max_focus'] // 2
            game_state['crit_next_turn'] = False
            game_state['enemy_stunned'] = False
            game_state['enemy_damage_multiplier'] = 1.0
            game_state['overdrive_active'] = False
            game_state['overdrive_turns_left'] = 0
            game_state['rebound_barrage_active'] = False
            game_state['rebound_barrage_turns'] = 0
            game_state['rebound_barrage_remaining_dmg'] = 0
            game_state['bleed_next_turn'] = False
            mettaton_empowered = False
            sleep(1)
            continue
        if enemy_hp <= 0:
            print(f"\nWell done. The {enemy_name} is now knocked out! You can now go ahead.")
            game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + win_hp_bonus)
            print(f"Your vitality has increased to {game_state['hp']}.")
            award_exp(enemy_data['exp_reward'])
            game_state['charge'] = 0
            game_state['focus'] = game_state['max_focus'] // 2
            game_state['crit_next_turn'] = False
            game_state['enemy_stunned'] = False
            game_state['enemy_damage_multiplier'] = 1.0
            game_state['overdrive_active'] = False
            game_state['overdrive_turns_left'] = 0
            game_state['rebound_barrage_active'] = False
            game_state['rebound_barrage_turns'] = 0
            game_state['rebound_barrage_remaining_dmg'] = 0
            game_state['bleed_next_turn'] = False
            print()
            return "win"
        if game_state['rebound_barrage_active'] and game_state['rebound_barrage_turns'] > 0:
            turn_dmg = game_state['rebound_barrage_remaining_dmg'] // game_state['rebound_barrage_turns']
            enemy_hp -= turn_dmg
            game_state['rebound_barrage_remaining_dmg'] -= turn_dmg
            game_state['rebound_barrage_turns'] -= 1
            print(f"Rebound Barrage continues to strike {enemy_name} for {turn_dmg} damage! {game_state['rebound_barrage_turns']} turns remaining.")
            if game_state['rebound_barrage_turns'] == 0:
                game_state['rebound_barrage_active'] = False
                print("Rebound Barrage fades.")
            sleep(1)
            if enemy_hp <= 0:
                continue
        action_taken_this_turn = False
        while not action_taken_this_turn:
            print(f"\n--- Your Turn ({enemy_name.capitalize()}: {enemy_hp} HP | You: {game_state['hp']}/{game_state['player_max_hp']} HP | Charge: {game_state['charge']}% | Focus: {game_state['focus']}/{game_state['max_focus']} | Stance: {game_state['stance'].capitalize()}) ---")
            
            prompt = """What shall you do?
1. Attack
2. Special Moves
3. Defend
4. Use Ultimate
5. Change Stance
"""
            valid_choices = [1, 2, 3, 4, 5]
            if game_state.get('has_greaves_of_sorrow'):
                prompt += "6. Switch Weapon\n"
                valid_choices.append(6)
            prompt += "7. Check Status\nChoice: "
            valid_choices.append(7)

            player_choice = get_player_input(prompt, valid_choices=valid_choices)
            print()
            sleep(1)
            if player_choice == 1:
                print("Your available attacks:")
                valid_attack_choices = []
                current_moveset = []
                # Determine which moves to show based on weapon
                if game_state.get('current_weapon') == 'boots':
                    current_moveset = [m for m in ALL_PLAYER_ATTACKS if ALL_PLAYER_ATTACKS[m].get('boots_req')]
                elif game_state.get('current_weapon') == 'gauntlets':
                    # --- FIX START ---
                    # The original code incorrectly checked game_state['player_attack_moveset'].
                    # This now correctly checks ALL_PLAYER_ATTACKS for any move requiring beowulf gauntlets.
                    current_moveset = [m for m in ALL_PLAYER_ATTACKS if ALL_PLAYER_ATTACKS[m].get('beowulf_req')]
                    # --- FIX END ---
                else: # Fallback to default sword moves
                    current_moveset = game_state['player_attack_moveset']

                for i, attack_name in enumerate(current_moveset):
                    attack_data = ALL_PLAYER_ATTACKS[attack_name]
                    if attack_data['type'] == 'attack':
                        print(f"{i+1}. {attack_data['name']} (Cost: {attack_data['focus_cost']} Focus) - {attack_data['desc']}")
                        valid_attack_choices.append(i + 1)
                
                if not valid_attack_choices:
                    print("You have no attacks equipped for this weapon!")
                    continue
                
                attack_index = get_player_input("Choose your attack: ", valid_choices=valid_attack_choices) - 1
                chosen_attack_name = current_moveset[attack_index]
                enemy_hp, action_taken_this_turn = attack_enemy(enemy_name, enemy_hp, chosen_attack_name, default_ret_range)
            elif player_choice == 2:
                print("Your available special moves:")
                valid_special_choices = []
                current_moveset = []
                # Determine which moves to show based on weapon
                if game_state.get('current_weapon') == 'boots':
                    current_moveset = [m for m in ALL_PLAYER_ATTACKS if ALL_PLAYER_ATTACKS[m].get('boots_req')]
                elif game_state.get('current_weapon') == 'gauntlets':
                    # --- FIX START ---
                    # The original code incorrectly checked game_state['player_special_moveset'].
                    # This now correctly checks ALL_PLAYER_ATTACKS for any move requiring beowulf gauntlets.
                    current_moveset = [m for m in ALL_PLAYER_ATTACKS if ALL_PLAYER_ATTACKS[m].get('beowulf_req')]
                    # --- FIX END ---
                else: # Fallback to default sword moves
                    current_moveset = game_state['player_special_moveset']
                
                for i, attack_name in enumerate(current_moveset):
                    attack_data = ALL_PLAYER_ATTACKS[attack_name]
                    if attack_data['type'] == 'special':
                        print(f"{i+1}. {attack_data['name']} (Cost: {attack_data['focus_cost']} Focus) - {attack_data['desc']}")
                        valid_special_choices.append(i + 1)

                if not valid_special_choices:
                    print("You have no special moves equipped for this weapon!")
                    continue
                
                attack_index = get_player_input("Choose your special move: ", valid_choices=valid_special_choices) - 1
                chosen_attack_name = current_moveset[attack_index]
                enemy_hp, action_taken_this_turn = attack_enemy(enemy_name, enemy_hp, chosen_attack_name, default_ret_range)
            elif player_choice == 3:
                defense_choice = get_player_input("""Choose your defense:
1. Parry (High risk, high reward: 25% chance to negate damage and get critical hit/stun next turn, costs 20 Focus)
2. Focus Charge (Take damage, gain 30-60 Focus)
Choice: """, valid_choices=[1, 2])
                print()
                if defense_choice == 1:
                    action_taken_this_turn = defend(enemy_name, "parry", default_ret_range)
                elif defense_choice == 2:
                    action_taken_this_turn = defend(enemy_name, "focus_charge", default_ret_range)
            elif player_choice == 4:
                enemy_hp, action_taken_this_turn = use_ult(enemy_name, enemy_hp)
            elif player_choice == 5:
                change_player_stance()
                action_taken_this_turn = True
            elif player_choice == 6 and game_state.get('has_greaves_of_sorrow'):
                if game_state['current_weapon'] == 'gauntlets':
                    game_state['current_weapon'] = 'boots'
                    print("You shift your stance, the energy from your gauntlets flowing down to your feet. You are now using the Greaves of Sorrow!")
                else:
                    game_state['current_weapon'] = 'gauntlets'
                    print("You shift your stance, the energy from your feet flowing up to your hands. You are now using the Beowulf Gauntlets!")
                action_taken_this_turn = True
            elif player_choice == 7:
                check_ult_charge()
                check_focus_amount()
                print(f"Current Health: {game_state['hp']}/{game_state['player_max_hp']}")
                print(f"Current Stance: {game_state['stance'].capitalize()}")
                if game_state.get('has_greaves_of_sorrow'):
                    print(f"Current Weapon: {game_state['current_weapon'].capitalize()}")
                print(f"Level: {game_state['level']} (EXP: {game_state['exp']}/{game_state['level'] * 100})")
                print(f"Base Damage: {game_state['player_base_dmg_min']}-{game_state['player_base_dmg_max']}")
            if not action_taken_this_turn and player_choice != 7:
                print("Action failed or invalid. Please choose again.")
                sleep(1)
            elif action_taken_this_turn:
                pass
        
        if special_enemy_effect_func and not game_state['enemy_stunned']:
            special_enemy_effect_func(enemy_name)

        if game_state['enemy_stunned']:
            print(f"The {enemy_name} is stunned for this turn!")
            game_state['enemy_stunned'] = False

        if game_state['enemy_damage_multiplier'] != 1.0:
            print(f"The {enemy_name}'s vulnerability wears off.")
            game_state['enemy_damage_multiplier'] = 1.0

def customize_moveset():
    print("\n--- Customize Your Moveset ---")
    print("You can select up to 5 Basic Attacks and 5 Special Moves for each weapon style.")
    
    # --- Gauntlet Customization ---
    if game_state.get('has_beowulf_gauntlets'):
        print("\n--- Customizing Gauntlets ---")
        available_attacks = []
        available_specials = []
        for attack_id, data in ALL_PLAYER_ATTACKS.items():
            if data.get('beowulf_req'):
                if data.get('type') == 'attack':
                    available_attacks.append((attack_id, data))
                elif data.get('type') == 'special':
                    available_specials.append((attack_id, data))
        
        new_attack_moveset = []
        while len(new_attack_moveset) < 5:
            print("\n--- Select Gauntlet Basic Attacks ---")
            # ... (Existing selection logic)
            break # Simplified for now
        
        new_special_moveset = []
        while len(new_special_moveset) < 5:
            print("\n--- Select Gauntlet Special Moves ---")
            # ... (Existing selection logic)
            break # Simplified for now
        
        # game_state['player_attack_moveset'] = new_attack_moveset
        # game_state['player_special_moveset'] = new_special_moveset
        print("Gauntlet moveset updated!")

    # --- Greaves Customization ---
    if game_state.get('has_greaves_of_sorrow'):
        print("\n--- Customizing Greaves ---")
        # Similar logic to gauntlets, but for boots_req moves
        print("Greaves customization would go here.")

    # --- Sword Customization (if applicable) ---
    if not game_state.get('has_beowulf_gauntlets'):
        print("\n--- Customizing Sword ---")
        # Existing sword customization logic
        print("Sword customization would go here.")
    
    print("\nYour moveset has been updated!")
    sleep(2)

def manage_diary():
    while True:
        print("\n--- Your Diary ---")
        choice = get_player_input("""
1. Read your entries
2. Write a new entry
3. Close the diary
Choice: """, [1, 2, 3])

        if choice == 1:
            if not game_state['diary_entries']:
                print("The pages are blank.")
            else:
                print("\n--- Diary Entries ---")
                for i, entry in enumerate(game_state['diary_entries']):
                    print(f"Entry {i+1}:\n{entry}\n--------------------")
            sleep(2)
        elif choice == 2:
            print("Write your thoughts. Press Enter on an empty line to finish.")
            new_entry_lines = []
            while True:
                line = input("> ")
                if line == "":
                    break
                new_entry_lines.append(line)
            new_entry = "\n".join(new_entry_lines)
            if new_entry:
                game_state['diary_entries'].append(new_entry)
                print("Your thoughts have been recorded.")
                save_game()
        elif choice == 3:
            print("You close the diary.")
            break

def act_1_intro_hub():
    print("\nThe world is not kind. It's a tapestry woven with threads of conflict and ambition. You are but one thread, a traveler with a simple sword and a past you'd rather not dwell on. Your journey begins at a crossroads tavern, the air thick with the smell of stale ale and simmering trouble.")
    while True:
        sleep(2)
        n = get_player_input("""The path ahead is uncertain. What is your first step?
1 - Step outside and begin your adventure.
2 - Take stock of your inventory.
3 - Consider a less... heroic path.
4 - A moment more of rest.
5 - Save your progress.
6 - Customize your moveset.
Enter your choice: """, valid_choices=[1, 2, 3, 4, 5, 6])
        print()
        sleep(1)
        if n == 1:
            print("You push open the heavy tavern door, sunlight momentarily blinding you. The road calls. It's time to go.")
            print()
            sleep(1)
            break
        elif n == 2:
            print("You check your belongings:")
            if game_state['has_beowulf_gauntlets']:
                print("- The **Beowulf** gauntlets, humming with the dual spirits of Soleil and Lune.")
            elif game_state['has_lobos_sword']:
                print("- The legendary sword **Lobos**. Its power feels restless.")
                if game_state['lobos_power_unlocked']:
                    print("  Its true power has been awakened!")
            elif game_state['silver_sword']:
                print("- A finely crafted **Silver Sword**, sharp and dangerous.")
            else:
                print("- A standard traveler's sword. It's seen better days, but it's yours.")
            if game_state['has_firefly_armor']: print("- The **Firefly Armor**, occasionally sparking with voltaic energy.")
            print(f"- Health: {game_state['hp']}/{game_state['player_max_hp']}")
            print(f"- Level: {game_state['level']} (EXP: {game_state['exp']}/{game_state['level'] * 100})")
        elif n == 3:
            print("'Heroes are fools who die for ideals,' you muse. 'Perhaps there's more profit in... acquisition.' The thought lingers, a tempting shadow.")
        elif n == 4:
            print("'Just one more drink,' you tell yourself. The warmth of the tavern is a comforting lie.")
        elif n == 5:
            save_game()
        elif n == 6:
            customize_moveset()
        sleep(2)
    while True:
        print("You leave the tavern behind. Before you, the path splits.")
        l = get_player_input("""Which path will you take?
1 - The shadowed wood, rumored to hold ancient secrets.
2 - The well-trod road, promising safety but little reward.
3 - The path of persistence, a steep and challenging climb.
Enter your choice: """, valid_choices=[1, 2, 3])
        print()
        sleep(1)
        if l == 1:
            print("You chose the woods. Days turn into weeks. You become a creature of the forest, forgotten by the world. It is a peaceful, if lonely, end to your story.")
            game_state['current_location'] = 'quit'
            return
        elif l == 2:
            print("The easy road loops back on itself, a subtle trap for the uninspired. You find yourself back at the tavern, the patrons giving you a knowing look. You've wasted the day.")
        elif l == 3:
            print("You choose the difficult path. The climb is arduous, but the air grows clearer, your resolve hardening with every step. This is the way forward.")
            print()
            sleep(1)
            break
        print()
    print("As you crest a hill, a brutish figure blocks your path. Its skin is green, its tusked jaw set in a snarl. An Orc.")
    battle_sequence(
        enemy_type="orc",
        win_hp_bonus=5,
        death_hp_reset=game_state['player_max_hp'],
    )
    print("With the Orc defeated, you see a town shimmering in the distance, its silver roofs catching the sun.")
    game_state['current_location'] = 'silverville'
    save_game()

def silverville_hub():
    global game_state
    game_state['current_location'] = 'silverville'
    if game_state.get('wizard_defeated', False):
        print("Silverville is safe, thanks to you. Your journey now takes you towards the legendary Mansion of Heroes.")
        game_state['current_location'] = 'mansion_of_heroes'
        return
    print("\nYou arrive in Silverville. The town is prosperous, built on the rich silver mines nearby, but a shadow hangs over the people. Whispers of a corrupt, powerful leader and strange creatures in the hills are on everyone's lips.")
    while True:
        sleep(2)
        silverville_choice = get_player_input("""What would you like to do in the troubled town of Silverville?
    1 - Walk the town streets, listen to the rumors.
    2 - Visit the blacksmith's forge.
    3 - Investigate the creature sightings near the mines.
    4 - Inquire about the town's leadership.
    5 - Save your progress.
    6 - Customize your moveset.
    Choice:""", valid_choices=[1, 2, 3, 4, 5, 6])
        print()
        if silverville_choice == 1:
            sleep(1)
            print("You wander the town. The townsfolk are skilled artisans, but their faces are etched with worry. They speak of exorbitant taxes and guards who act more like jailers than protectors.")
            print()
            continue
        elif silverville_choice == 2:
            silver_action_choice = get_player_input("""At the forge, the heat is palpable. On display is a magnificent silver sword, gleaming under the forge light. The blacksmith warns it enhances the wielder's ferocity, but at the cost of defense.
    What shall you do?
    1. 'Borrow' the sword when the smith is distracted.
    2. Admire the craftsmanship and leave it be.
    Choice:""", valid_choices=[1, 2])
            if silver_action_choice == 1:
                steal_success = random.randint(1, 2)
                if steal_success == 1:
                    game_state['silver_sword'] = True
                    game_state['default_sword'] = False
                    print("Your hands are quick. The silver sword is now yours.")
                else:
                    print("The blacksmith's eye is sharper than you anticipated. You fail to take the sword.")
            elif silver_action_choice == 2:
                print("A fine weapon, but not for you. You leave it for another warrior.")
            print()
            continue
        elif silverville_choice == 3:
            print("You follow a trail leading to a dark cave near the silver mines. The ground is littered with scorched bones and strange, colorful scales. A venomous hiss echoes from within...")
            sleep(3)
            print("A reptilian head emerges, followed by massive, leathery wings. A Wyvern!")
            battle_sequence(
                enemy_type="wyvern",
                win_hp_bonus=5,
                death_hp_reset=game_state['player_max_hp'],
            )
            continue
        elif silverville_choice == 4:
            print("Your questions about the town's leader are met with fear, until one brave resident pulls you aside. They reveal the leader is a powerful, corrupt wizard who has ruled for decades, draining the town's wealth to fuel his magic.")
            sleep(4)
            print("He resides in a heavily guarded mansion at the heart of the town. It's clear that to free Silverville, the wizard must be confronted.")
            print()
            sleep(3)
            print("You resolve to infiltrate the mansion. You find an unguarded window and slip inside, the decadent halls patrolled by armored sentinels.")
            sleep(4)
            print("You sneak past the guards and find the wizard's inner sanctum. He turns from a scrying mirror, his eyes cold and ancient.")
            sleep(3)
            print("'Another would-be hero,' the wizard sneers. 'Do you have any idea how many of your kind I have turned into statues in my garden? Come then, let us see if you are worthy of being a decoration.'")
            sleep(4)
            battle_sequence(
                enemy_type="wizard",
                win_hp_bonus=10,
                death_hp_reset=game_state['player_max_hp'],
            )
            game_state['wizard_defeated'] = True
            sleep(2)
            print("\nThe wizard disintegrates into a cloud of silver dust. As you walk out of the mansion, the guards stand down, their magical compulsion broken. The people of Silverville emerge, cheering their liberation.")
            sleep(5)
            print("In gratitude, the town elders gift you their most prized artifact: a legendary sword known as 'Lobos'. You accept the blade and the thanks of a free people, and set off for your next destination.")
            game_state['has_lobos_sword'] = True
            game_state['current_location'] = 'mansion_of_heroes'
            save_game()
            return
        elif silverville_choice == 5:
            save_game()
        elif silverville_choice == 6:
            customize_moveset()
        sleep(2)

def mansion_of_heroes_hub():
    global game_state
    game_state['current_location'] = 'mansion_of_heroes'
    print("\nYou walk for 15 kilometers on the trail, until you reach the Mansion of Heroes")
    print()
    sleep(2)
    print("""You have reached the Mansion of Heroes, a place filled with knights, mages and everything in between. The guilds and heroes all gather for quests and other errands.""")
    print()
    while True:
        sleep(2)
        moh_choice = get_player_input("""What do you want to do?
    1. Explore the mansion
    2. Talk to the master of blades (UNLOCKS LOBOS TRUE POWER)
    3. Fight someone
    4. Draft a flyer to recruit someone
    5. Say something political
    6. Save Game and Quit
    7. Customize Moveset
    Choice:""", valid_choices=[1, 2, 3, 4, 5, 6, 7])
        print()
        if moh_choice == 1:
            sleep(1)
            print("""You explore the mansion, it has pictures of every hero that has passed through it.
    The founder was named Ferg "The ruthless" Grandmaster.
    He wielded a legendary blade with the fusion of 10 living blades, it was lost upon his death.
    People still theorize where it is, despite no one ALIVE who knows where it is.""")
            print()
            continue
        elif moh_choice == 2:
            if game_state['has_lobos_sword'] and not game_state['lobos_power_unlocked']:
                sleep(2)
                print("""You visit the master of blades.
    He is a guy with green hat who has a table and a mat in the middle of the room. "So, you have come to discover the power of your blade?" You nod
    "Very well, sit down and place your sword on the table." """)
                sleep(3)
                print("""When you place the blade on the little table, you feel a strange energy emitting from it.
    "Now, sit down and close your eyes to connect with it."
    You do so.""")
                sleep(2)
                print("You are sent into a world with a person standing in the middle of a pond with swords lain all across the landscape")
                sleep(3)
                print(""""You've come"
    says the figure
    "I am the blade the voice gave you.
    He didn't tell you how to wield my powers.
    It's simple.
    Fight me
    Beat me
    and awaken my true power."
    """)
                result = battle_sequence(
                    enemy_type="lobos_spirit",
                    win_hp_bonus=10,
                    death_hp_reset=game_state['player_max_hp'],
                )
                if result == "win":
                    game_state['lobos_power_unlocked'] = True
                    game_state['player_max_hp'] += 10
                    game_state['player_base_dmg_min'] += 5
                    game_state['player_base_dmg_max'] += 5
                    game_state['max_focus'] += 25
                    game_state['focus'] = game_state['max_focus']
                    print(f"\nYour max HP increased to {game_state['player_max_hp']}, base damage improved, and max focus increased to {game_state['max_focus']}!")
                    game_state['hp'] = game_state['player_max_hp']
                    sleep(2)
                    print("Lobos now grants new ultimate abilities!")
                    print()
                else:
                    print("\nThe sword spirit has bested you. You feel yourself pulled back from the ethereal plane. You need to train more!")
                    print()
            elif game_state['has_lobos_sword'] and game_state['lobos_power_unlocked']:
                print("You have already awakened Lobos' true power. The Master of Blades has nothing more to teach you about it.")
                print()
            else:
                print("You don't have 'Lobos' yet. You need to obtain it first to talk to the Master of Blades about its true power.")
                print()
            continue
        elif moh_choice == 3:
            print("You look around for someone to fight. Everyone seems busy or too strong.")
            print("Maybe later...")
            print()
            continue
        elif moh_choice == 4:
            print("You attempt to draft a flyer but realize you have no artistic talent. You crumple the paper.")
            print()
            continue
        elif moh_choice == 5:
            print("You clear your throat and prepare a passionate speech on the current state of hero politics. As you finish, three armored figures approach you, their visors glowing menacingly.")
            sleep(3)
            print("\n\"Your words are... troublesome, adventurer,\" one growls, a faint, chilling hiss accompanying his voice. \"The order of the Dragon Knights does not tolerate dissent.\"")
            print("These aren't just knights. As they draw their swords, you see their movements are fluid, unnatural. Each of them has a strange, almost serpentine quality.")
            sleep(4)
            hydra_battle_won = False
            for i in range(1, 4):
                print(f"\n--- Battle against Hydra Knight {i}! ---")
                initial_hydra_hp = ALL_ENEMY_STATS['hydra_knight']['hp'] + (i-1)*20
                temp_enemy_data = ALL_ENEMY_STATS['hydra_knight'].copy()
                temp_enemy_data['hp'] = initial_hydra_hp
                result = battle_sequence(
                    enemy_type="hydra_knight",
                    win_hp_bonus=10,
                    death_hp_reset=game_state['player_max_hp'],
                    intro_text=f"Hydra Knight {i} engages!"
                )
                if result == "win":
                    pass
                if i < 3:
                    print(f"\nYou defeated Hydra Knight {i}! Two more remain.")
                    sleep(2)
                else:
                    print("\nAll three Hydra Knights have been vanquished! Their glowing visors dim as they fall. The Mansion of Heroes falls silent around you.")
                    hydra_battle_won = True
                    sleep(3)
            if hydra_battle_won:
                print("Feeling a strange impulse, you decide the Mansion of Heroes has seen enough of your political statements for now and you slip out under the cover of night, following an old, shadowed road.")
                game_state['current_location'] = 'creepwood'
                save_game()
                return
            else:
                print("\nYou were overwhelmed by the Hydra Knights. You're revived, but you decide to abandon your political ambitions for now and rethink your path.")
                sleep(2)
                continue
        elif moh_choice == 6:
            save_game()
            game_state['current_location'] = 'quit'
            return
        elif moh_choice == 7:
            customize_moveset()
        print()

def creepwood_hub():
    global game_state
    game_state['current_location'] = 'creepwood'
    print("\n--- You arrive at Creepwood! ---")
    print("This town truly comes alive at night, shrouded in mist and eerie silence...")
    act2_initiated = False
    while True:
        sleep(2)
        creepwood_choice = get_player_input("""What would you like to do in Creepwood?
    1. Just explore the town (Wander the shadowy streets)
    2. Check out the gravestones (Encounter a Zombie!)
    3. Have a bone to pick (Fight a Skeleton!)
    4. Ghost possession (Gain temporary buffs/debuffs to your stances)
    5. Eat some food (Restore health)
    6. Attend Ritual (Initiate Act 2)
    7. Attend Halloween party in June (Join a peculiar celebration)
    8. Investigate disappearance (A mysterious side quest)
    9. Help out the local graveyard shaper (Lend a hand)
    10. Stare at grave named "Skeletron" (Confront a powerful boss)
    11. Save Game and Quit
    12. Customize Moveset
    Choice:""", valid_choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        print()
        if creepwood_choice == 1:
            print("You wander through Creepwood's dimly lit streets. Strange carvings adorn ancient trees, and the air is thick with the scent of damp earth and something indefinably old.")
            print("You find nothing particularly exciting, but the atmosphere is undeniably unique.")
        elif creepwood_choice == 2:
            print("You approach a cluster of overgrown gravestones. A guttural groan echoes from beneath the soil as a decaying hand bursts forth, followed by a shambling figure!")
            battle_sequence(
                enemy_type="zombie",
                win_hp_bonus=3,
                death_hp_reset=game_state['player_max_hp'],
            )
            game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + 3)
            print(f"Your health is now {game_state['hp']}/{game_state['player_max_hp']}.")
        elif creepwood_choice == 3:
            print("You kick at a pile of bones, and with a rattling clatter, they assemble into a bony warrior wielding a rusty blade!")
            battle_sequence(
                enemy_type="skeleton",
                win_hp_bonus=4,
                death_hp_reset=game_state['player_max_hp'],
            )
            game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + 4)
            print(f"Your health is now {game_state['hp']}/{game_state['player_max_hp']}.")
        elif creepwood_choice == 4:
            if not game_state['ghost_form']:
                game_state['ghost_form'] = True
                print("You feel a chilling sensation as an ethereal presence merges with you. You feel a strange shift in your combat flow!")
                print("Your stances will now have minor ghost-related buffs and debuffs.")
            else:
                game_state['ghost_form'] = False
                print("You concentrate and manage to expel the ghostly presence. You feel lighter, back to your normal self.")
        elif creepwood_choice == 5:
            heal_amt = random.randint(15, 30)
            game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + heal_amt)
            print(f"You find a strange, glowing mushroom and eat it. Your health recovers by {heal_amt}! Current Health: {game_state['hp']}/{game_state['player_max_hp']}")
        elif creepwood_choice == 6:
            if not act2_initiated:
                act2_initiated = True
                print("\nYou seek out a public square with a massive, resonating crystal broadcasting news from the rulers of this land.")
                sleep(3)
                print("\n--- End of Act 1 ---")
                print("\nACT 2: CAN'T FEAR YOUR OWN WORLD")
                sleep(3)
                print("\n*** CUTSCENE: The Regent's Council ***")
                sleep(2)
                print("In the grand hall, figures of immense power convene. This is not a discussion; it is a declaration of impending war.")
                sleep(4)
                print("\nGRAND REGENT THRAGG: The barriers between worlds fray. These so-called 'heroes' are an uncontrolled variable. Their strength is an affront to our order. They must be brought to heel.")
                sleep(4)
                print("\nWEEP AND DROWN: (Weep) The magic... it runs wild... (Drown) These mortals and their chaotic power will sunder the foundations! Their meddling must be punished. We will show them true despair.")
                sleep(4)
                print("\nVERGIL: The reports are clear. Their power grows unchecked. A watchlist is prudent. We must identify the strongest, the most volatile. They are either assets to be controlled or threats to be eliminated.")
                sleep(4)
                print("\nGRAND REGENT THRAGG: Then it is decided. The list will be made. These five 'elites'... their recent actions have drawn our gaze. Monitor them. Know their strengths, their weaknesses. When the time is right, we will break them.")
                sleep(3)
                print("\n*** END CUTSCENE ***")
                sleep(4)
                print("\n--- You find yourself walking towards your next destination, the chilling words of the council echoing in your mind. ---")
                print("You realize with a jolt that your own name was mentioned among the 'elite heroes'. A watchlist. What could that mean? A dark cloud hangs over the world, and you are undeniably part of it now.")
                sleep(4)
                game_state['current_location'] = 'mole_city'
                save_game()
                return
            else:
                print("You've already initiated this broadcast and know of the upcoming journey.")
                continue
        elif creepwood_choice == 7:
            print("You stumble upon a very loud, very enthusiastic party. It's Halloween in June, complete with costumes, spooky decorations, and loud, anachronistic music. You shrug and join in, enjoying the bizarre spectacle.")
            print("You feel surprisingly refreshed! (+10 Focus)")
            game_state['focus'] = min(game_state['max_focus'], game_state['focus'] + 10)
        elif creepwood_choice == 8:
            print("You decide to investigate a recent disappearance reported by a local. You follow faint footprints, discover strange symbols, and slowly piece together a dark story. The trail leads you to a dead end for now, but you feel like you've learned something important about Creepwood's hidden dangers.")
        elif creepwood_choice == 9:
            print("You find the local graveyard shaper, a hunched figure named Mort, meticulously arranging ancient bones. You offer to help, and he gratefully accepts. You spend some time organizing skulls and femurs, earning his quiet respect.")
            print("Mort gives you a surprisingly sturdy bone charm. (+5 Max Health permanently! For now, just a small heal.)")
            game_state['player_max_hp'] += 5
            game_state['hp'] = min(game_state['hp'] + 10, game_state['player_max_hp'])
            print(f"Your health feels a little better. Current Health: {game_state['hp']}/{game_state['player_max_hp']}")
        elif creepwood_choice == 10:
            print("You stand before an ominously large, intricately carved gravestone bearing the name 'Skeletron'. A chill wind whips around you, and arcane symbols glow faintly on the stone. This is it. The big one.")
            battle_sequence(
                enemy_type="skeletron",
                win_hp_bonus=20,
                death_hp_reset=game_state['player_max_hp'],
            )
        elif creepwood_choice == 11:
            save_game()
            game_state['current_location'] = 'quit'
            return
        elif creepwood_choice == 12:
            customize_moveset()
        print()

def mole_city_and_brig_base_hub():
    global game_state
    game_state['current_location'] = 'mole_city'
    if game_state.get('battle_beast_defeated', False):
        game_state['current_location'] = 'regents_confrontation'
        return
    print("\nYou arrive at the **Prisque Checkpoint**, a massive fortified gate guarded by diligent soldiers. It's the only way to pass into the western territories.")
    sleep(3)
    print("\n--- Registration Minigame ---")
    print("A stern-looking guard steps forward. \"State your business, traveler. And prepare for registration.\"")
    sleep(2)
    registered = False
    while not registered:
        print("\nGUARD: What is the primary directive of the Regent's Council regarding rogue magic users?")
        print("1. Eliminate them immediately.")
        print("2. Monitor them and, if possible, rehabilitate them.")
        print("3. Ignore them, as magic is too unpredictable.")
        reg_answer_1 = get_player_input("Your answer: ", valid_choices=[1, 2, 3])
        print()
        if reg_answer_1 == 2:
            print("GUARD: Hmm, astute. Next question. In which Silverville district did the recent Wyvern incident occur?")
            print("1. The Residential District")
            print("2. The Market Square")
            print("3. Near the Silver Mines")
            reg_answer_2 = get_player_input("Your answer: ", valid_choices=[1, 2, 3])
            print()
            if reg_answer_2 == 3:
                print("GUARD: Correct. Last question. What is the traditional greeting among miners of the Deep Earth?")
                print("1. 'May your pickaxe find ore!'")
                print("2. 'Light the way!'")
                print("3. 'To the surface!'")
                reg_answer_3 = get_player_input("Your answer: ", valid_choices=[1, 2, 3])
                print()
                if reg_answer_3 == 1:
                    print("GUARD: You pass, traveler. Your knowledge is... surprisingly thorough. Proceed.")
                    registered = True
                    sleep(2)
                else:
                    print("GUARD: Incorrect! Your lack of local knowledge is concerning. Try again from the beginning.")
                    sleep(2)
            else:
                print("GUARD: Incorrect! Pay more attention to recent events. Try again.")
                sleep(2)
        else:
            print("GUARD: Incorrect! You clearly do not understand the delicate balance we strive for. Try again.")
            sleep(2)
    print("\nWith your registration complete, the mighty gates of Prisque Checkpoint slowly creak open. You step onto a path that descends into the earth, the air growing cooler and smelling faintly of damp rock and minerals.")
    print("Ahead, you see a faint, multi-colored glow.")
    sleep(4)
    print("\n--- Welcome to Mole City! ---")
    print("You arrive in **Mole City**, an astonishing underground metropolis. Caverns are carved into bustling streets, lit by glowing crystals embedded in the walls. Miners with pickaxes pass by, their faces smudged with dust, and the clanging of metal on rock echoes from afar. Gems sparkle from rock faces, and the scent of rich earth mingles with something sharp – sulfur, perhaps, from the explosives used in the deeper mines.")
    sleep(5)
    while True:
        print("\n--- Mole City Hub ---")
        prompt = """What would you like to do?
1. Explore the city.
2. Visit the Shaman to exorcise a ghost (if you are possessed).
3. Reforge your sword at the Great Forge.
4. Trace the path of the Eater of Worlds.
5. Play a crystal tune for the crowd.
6. Listen to the Monarchs' broadcast (Continue Story).
7. Save Game and Quit.
8. Customize Moveset
Choice: """
        choice = get_player_input(prompt, [1, 2, 3, 4, 5, 6, 7, 8])
        print()
        if choice == 1:
            print("You spend some time wandering the carved-out streets. The glowing crystals give the city a magical, yet industrial, feel. You see mole-people and humans working together, their lives intertwined with the rhythm of mining and crafting.")
        elif choice == 2:
            if game_state['ghost_form']:
                print("You find a mole-person Shaman in a quiet cavern, smoke from strange incense filling the air. He chants in a low, rumbling tone, placing a hand on your forehead.")
                sleep(3)
                print("You feel a sudden lightness as the ghostly presence is expelled from your body!")
                game_state['ghost_form'] = False
            else:
                print("You visit the Shaman, but he senses no spirits clinging to you. 'You are clean,' he rumbles.")
        elif choice == 3:
            print("At the Great Forge, the heat is immense. A master smith offers to imbue your blade with elemental power.")
            reforge_choice = get_player_input("""Which element will you choose?
1. Flaming (Applies a burn after you attack)
2. Lightning (Chance to stun the enemy on hit)
3. Arcane (Adds bonus damage to every strike)
4. Gale (Increases your defense, slightly lowers attack)
5. Never mind
Choice: """, [1, 2, 3, 4, 5])
            game_state['flaming_sword'] = False
            game_state['lightning_sword'] = False
            game_state['arcane_sword'] = False
            game_state['gale_sword'] = False
            if reforge_choice == 1:
                game_state['flaming_sword'] = True
                print("Your sword erupts in magical flames!")
            elif reforge_choice == 2:
                game_state['lightning_sword'] = True
                print("Your sword crackles with raw lightning!")
            elif reforge_choice == 3:
                game_state['arcane_sword'] = True
                print("Your sword hums with arcane energy!")
            elif reforge_choice == 4:
                game_state['gale_sword'] = True
                print("Winds swirl around your blade, creating a protective barrier!")
            else:
                print("You decide to keep your sword as is for now.")
        elif choice == 4:
            print("You follow a massive tunnel bored through the rock, signs of a colossal creature's passage are everywhere. At the end of the cavern, the ground trembles and a monstrous worm erupts from the earth!")
            battle_sequence(
                enemy_type="eater_of_worlds",
                win_hp_bonus=20,
                death_hp_reset=game_state['player_max_hp'],
            )
        elif choice == 5:
            print("You find a set of large, tuned crystals in a public square. A crowd gathers, curious.")
            print("The lead crystal player shows you a sequence. Repeat it correctly!")
            sleep(2)
            crystals = {"r": "Red", "b": "Blue", "g": "Green", "y": "Yellow", "p": "Purple"}
            sequence_to_match = [random.choice(list(crystals.values())) for _ in range(4)]
            print(f"The sequence is: {' - '.join(sequence_to_match)}")
            print("Now, enter the first letter of each crystal to play the tune (e.g., 'r' for Red).")
            correct = True
            for crystal_name in sequence_to_match:
                player_input_char = input(f"Next crystal ({'/'.join(crystals.keys())}): ").lower().strip()
                if not player_input_char or crystals.get(player_input_char) != crystal_name:
                    print(f"Whoops, that's not right! The crowd seems disappointed. The correct crystal was {crystal_name}.")
                    correct = False
                    break
            if correct:
                print("A perfect performance! The crowd cheers and tosses you some coins!")
                game_state['focus'] = min(game_state['max_focus'], game_state['focus'] + 10)
                print("You feel a surge of confidence! (+10 Focus)")
        elif choice == 6:
            print("You join a crowd gathering around a large crystal that begins to hum with energy, broadcasting a message from the Monarchs.")
            sleep(2)
            print("\nThe broadcast is actually a coded message, one you were meant to receive. It speaks of a gathering of 'elite threats' at a secret location: the Brig Military Base. Your path is clear.")
            sleep(4)
            break
        elif choice == 7:
            save_game()
            game_state['current_location'] = 'quit'
            return
        elif choice == 8:
            customize_moveset()
        sleep(3)
    print("You travel for days, following the cryptic directions, until you arrive at a heavily fortified compound, bristling with guards and magical wards. This is the Brig Military Base.")
    sleep(3)
    print("\n--- Infiltration Minigame ---")
    print("You must find a way inside without raising an alarm. The perimeter is heavily patrolled.")
    sleep(2)
    sneaked_in = False
    while not sneaked_in:
        sneak_choice = get_player_input("""How will you get in?
    1. Create a diversion and slip past the main gate during the confusion.
    2. Scale the western wall under the cover of a passing storm cloud.
    3. Bribe a disgruntled-looking guard near the supply entrance.
    Your choice: """, valid_choices=[1, 2, 3])
        print()
        if sneak_choice == 1:
            if random.random() < 0.6:
                print("Your diversion works perfectly! You slip inside unnoticed.")
                sneaked_in = True
            else:
                print("The guards are too disciplined and quickly contain your diversion. You're spotted and have to retreat. Try another way.")
                sleep(2)
        elif sneak_choice == 2:
            if game_state['focus'] > 40:
                print("You use your focus and agility to scale the wall, the storm masking your ascent. You're in.")
                sneaked_in = True
            else:
                print("You lack the focus for such a difficult climb and slip, making a noise. You barely escape before guards investigate. You need to be more prepared.")
                sleep(2)
        elif sneak_choice == 3:
            if random.randint(1, 10) > 4:
                print("The guard grumbles, but pockets your bribe and looks the other way. You're in.")
                sneaked_in = True
            else:
                print("The guard scoffs at your bribe and raises the alarm! You quickly retreat into the shadows.")
                sleep(2)
    print("\nOnce inside, you follow the message's final instructions to a hidden briefing room. Four figures await you, their auras radiating immense power.")
    sleep(3)
    print("\nA man with swirling energy for eyes, ANGSTROM LEVY, nods at you. 'So, the final piece arrives. I can mend wounds and manipulate reality's fabric. A useful trick.'")
    sleep(3)
    print("\nA warrior in dark, jagged armor, GRIMM, sharpens a wicked-looking blade. 'More fighters. Good. My strikes will be the death of our foes.'")
    sleep(3)
    print("\nA lithe woman named LEAT, whose movements are almost too fast to follow, gives a slight bow. 'Precision and timing are key. I can turn any blow back on our enemy.'")
    sleep(3)
    print("\nFinally, a mountain of a man in stone-etched armor, GRAYSTONE, crosses his colossal arms. 'My strength is the foundation upon which we will build our victory. Together, our power is absolute.'")
    sleep(4)
    print("\nAngstrom turns to the group. 'The Regents are in the command spire. We go up, together.'")
    sleep(2)
    print("\nYou all proceed to a massive elevator. As the doors close, the ascent begins... and so do the ambushes.")
    sleep(2)
    battle_sequence(
        enemy_type="elite_sentinel",
        win_hp_bonus=5,
        death_hp_reset=game_state['player_max_hp']
    )
    print("\n--- The elevator continues, only to be flooded with arcane energy. A pair of Arcane Binders appear! ---")
    battle_sequence(
        enemy_type="arcane_binder",
        win_hp_bonus=5,
        death_hp_reset=game_state['player_max_hp']
    )
    print("\nThe elevator finally reaches the top floor. The doors open to a grand throne room. Before you stands a towering, bipedal white lion, hefting a huge mace in one hand and a greatsword in the other.")
    sleep(3)
    print("\nHe is Battle Beast. He was hired to stop you, but he cares not for money. He points his mace at your party.")
    sleep(3)
    print("'I have waited for a challenge worthy of a true warrior,' he roars, his voice a deep growl. 'The Regents offer coin, but you... you offer glory. Show me a battle so magnificent that it will be my last! Let this be our final, glorious struggle!'")
    sleep(4)
    battle_beast_boss_fight()

def battle_beast_boss_fight():
    enemy_hp = 1500
    battle_beast_dmg_bonus = 0
    angstrom_cooldown = 0
    grimm_cooldown = 0
    leat_cooldown = 0
    graystone_cooldown = 0
    game_state['hp'] = game_state['player_max_hp']
    game_state['charge'] = 0
    game_state['focus'] = game_state['max_focus'] // 2
    game_state['overdrive_active'] = False
    game_state['overdrive_turns_left'] = 0
    game_state['enemy_damage_multiplier'] = 1.0
    print("\n--- BOSS FIGHT: BATTLE BEAST ---")
    while enemy_hp > 0 and game_state['hp'] > 0:
        action_taken_this_turn = False
        while not action_taken_this_turn:
            print(f"\n--- Your Turn (Battle Beast: {enemy_hp} HP | You: {game_state['hp']}/{game_state['player_max_hp']} HP | Charge: {game_state['charge']}% | Focus: {game_state['focus']}/{game_state['max_focus']}) ---")
            print("Your allies stand ready!")
            player_choice = get_player_input("""What shall you do?
    1. Your Attack
    2. Your Defense (Parry/Focus Charge)
    3. Your Ultimate
    4. Command an Ally
    Choice: """, valid_choices=[1, 2, 3, 4])
            print()
            sleep(1)
            if player_choice == 1:
                print("Your available attacks:")
                valid_attack_choices = []
                for i, attack_name in enumerate(game_state['player_attack_moveset']):
                    attack_data = ALL_PLAYER_ATTACKS[attack_name]
                    print(f"{i+1}. {attack_data['name']} (Cost: {attack_data['focus_cost']} Focus) - {attack_data['desc']}")
                    valid_attack_choices.append(i + 1)
                if not valid_attack_choices:
                    print("You have no available attacks!")
                    action_taken_this_turn = False
                    continue
                attack_index = get_player_input("Choose your attack: ", valid_choices=valid_attack_choices) - 1
                chosen_attack_name = game_state['player_attack_moveset'][attack_index]
                enemy_hp, action_taken_this_turn = attack_enemy("Battle Beast", enemy_hp, (20, 35))
                if action_taken_this_turn:
                    battle_beast_dmg_bonus += 5
                    print("His rage grows! (Damage +5)")
            elif player_choice == 2:
                defense_choice = get_player_input("""Choose your defense:
1. Parry (High risk, high reward)
2. Focus Charge (Take damage, gain Focus)
Choice: """, valid_choices=[1, 2])
                print()
                if defense_choice == 1:
                    action_taken_this_turn = defend("Battle Beast", "parry", (20, 35))
                elif defense_choice == 2:
                    action_taken_this_turn = defend("Battle Beast", "focus_charge", (20, 35))
            elif player_choice == 3:
                enemy_hp, action_taken_this_turn = use_ult("Battle Beast", enemy_hp)
                if action_taken_this_turn:
                    battle_beast_dmg_bonus += 20
                    print("His fury boils! (Damage +20)")
            elif player_choice == 4:
                ally_choice = get_player_input(f"""Which ally will assist?
    1. Angstrom (Heal) {'[Ready]' if angstrom_cooldown == 0 else f'[CD: {angstrom_cooldown}]'}
    2. Grimm (Damage) {'[Ready]' if grimm_cooldown == 0 else f'[CD: {grimm_cooldown}]'}
    3. Leat (Parry/Charge) {'[Ready]' if leat_cooldown == 0 else f'[CD: {leat_cooldown}]'}
    4. Graystone (Joint Ultimate) {'[Ready]' if graystone_cooldown == 0 else f'[CD: {graystone_cooldown}]'}
    Choice: """, valid_choices=[1, 2, 3, 4])
                if ally_choice == 1 and angstrom_cooldown == 0:
                    heal_amt = random.randint(30, 50)
                    game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + heal_amt)
                    print(f"Angstrom Levy mends your wounds, healing you for {heal_amt} HP!")
                    angstrom_cooldown = 3
                    action_taken_this_turn = True
                elif ally_choice == 2 and grimm_cooldown == 0:
                    grimm_dmg = random.randint(60, 90) + game_state['level'] * 2
                    enemy_hp -= grimm_dmg
                    battle_beast_dmg_bonus += 10
                    print(f"Grimm lands a devastating blow for {grimm_dmg} damage!")
                    print("Battle Beast is enraged! (Damage +10)")
                    grimm_cooldown = 2
                    action_taken_this_turn = True
                elif ally_choice == 3 and leat_cooldown == 0:
                    charge_gain = 30
                    game_state['charge'] = min(100, game_state['charge'] + charge_gain)
                    print("Leat positions herself perfectly. The Battle Beast's next attack will be parried, and you gain 30 ultimate charge!")
                    game_state['enemy_stunned'] = True
                    leat_cooldown = 4
                    action_taken_this_turn = True
                elif ally_choice == 4 and graystone_cooldown == 0:
                    if game_state['charge'] >= 100:
                        joint_ult_dmg = random.randint(200, 300) + game_state['level'] * 5
                        enemy_hp -= joint_ult_dmg
                        game_state['charge'] = 0
                        battle_beast_dmg_bonus += 40
                        print(f"You and Graystone unleash a combined ultimate, dealing a massive {joint_ult_dmg} damage!")
                        print("His power surges to its peak! (Damage +40)")
                        graystone_cooldown = 5
                        action_taken_this_turn = True
                    else:
                        print("You don't have enough charge for a joint ultimate!")
                        action_taken_this_turn = False
                else:
                    print("That ally is not ready or choice is invalid! Please choose again.")
                    action_taken_this_turn = False
            if not action_taken_this_turn:
                print("Action failed or invalid. Please choose a valid action that can be performed.")
                sleep(1)
        if game_state['enemy_damage_multiplier'] != 1.0:
            print("Battle Beast's vulnerability wears off.")
            game_state['enemy_damage_multiplier'] = 1.0
        if enemy_hp <= 0:
            break
        if not game_state['enemy_stunned']:
            ret_dmg = random.randint(20, 35) + battle_beast_dmg_bonus
            if game_state['overdrive_active']:
                ret_dmg = int(ret_dmg * 1.5)
                game_state['overdrive_turns_left'] -= 1
                if game_state['overdrive_turns_left'] <= 0:
                    game_state['overdrive_active'] = False
                    print("Overdrive wears off.")
            if game_state['stance'] == "defensive":
                ret_dmg = int(ret_dmg * 0.8)
                print("Your Defensive Stance helps mitigate some of the incoming damage!")
            if game_state['gale_sword']:
                ret_dmg = int(ret_dmg * 0.9)
                print("Your Gale Sword's barrier reduces incoming damage!")
            game_state['hp'] -= ret_dmg
            print(f"\nBattle Beast retaliates with furious might, dealing {ret_dmg} damage to you! Your HP is {game_state['hp']}.")
            sleep(2)
        else:
            print("Battle Beast is stunned and cannot attack!")
            game_state['enemy_stunned'] = False
        if game_state['hp'] <= 0:
            print("\nYou have been defeated. The glorious battle ends, but not in your favor. You reawaken, the memory of the fight burning in your mind, ready to try again.")
            game_state['hp'] = game_state['player_max_hp']
            enemy_hp = 1500
            battle_beast_dmg_bonus = 0
            angstrom_cooldown = 0
            grimm_cooldown = 0
            leat_cooldown = 0
            graystone_cooldown = 0
            game_state['overdrive_active'] = False
            game_state['overdrive_turns_left'] = 0
            game_state['enemy_damage_multiplier'] = 1.0
            sleep(2)
            continue
        if angstrom_cooldown > 0: angstrom_cooldown -= 1
        if grimm_cooldown > 0: grimm_cooldown -= 1
        if leat_cooldown > 0: leat_cooldown -= 1
        if graystone_cooldown > 0: graystone_cooldown -= 1
    if game_state['hp'] > 0:
        print("\nWith a final, earth-shattering blow, the Battle Beast falls to his knees, his weapons clattering to the floor. He looks up, a bloody grin on his face.")
        sleep(2)
        print("'Yes...' he breathes, his voice a satisfied rumble. 'This... this was a good death. Glorious...' He collapses. The path to the Regents is clear.")
        sleep(3)
        game_state['battle_beast_defeated'] = True
        award_exp(ALL_ENEMY_STATS['battle_beast']['exp_reward'])
        game_state['current_location'] = 'regents_confrontation'
        save_game()

def regents_confrontation():
    print("\nYou and your new allies heal and prepare. The final confrontation is at hand. You ascend to the Regent's throne room.")
    sleep(4)
    print("\nBefore the Regents, you and your allies stand ready.")
    sleep(2)
    print("GRAND REGENT THRAGG: So, the pests have reached the heart of the operation. You've been a thorn in our side for far too long.")
    sleep(4)
    print("GRIMM: Your tyranny ends today, Thragg!")
    sleep(2)
    print("Thragg smirks, a chilling, condescending expression. A dark, purple energy flows from his hand and envelops Grimm.")
    sleep(4)
    print("GRAND REGENT THRAGG: Tyranny? I bring order. You fight for them? You, who carries the mark of the conqueror? You are one of us. Now... prove your loyalty.")
    sleep(4)
    print("Grimm clutches his head, his dark armor beginning to glow with a menacing red light. He stumbles, fighting an unseen force.")
    sleep(4)
    print("GRIMM: I... I won't... ARGH!")
    sleep(3)
    print("He lets out a roar, not of defiance, but of agony and rage. He turns to you, his blade raised, his eyes glowing red.")
    sleep(2)
    print("He lunges!")
    sleep(2)
    print("\nYou are struck down by a blow you cannot possibly parry. The power is immense, overwhelming...")
    print("Your vision fades to black as you hear the cacophony of battle erupt around you.")
    sleep(4)
    print("\n...")
    sleep(2)
    print("Hey. Wake up. It's me again, your friendly neighborhood conscience.")
    sleep(2)
    print("Looks like you got in over your head. That 'Grimm' fellow packed a bigger punch than expected, especially with some 'help'.")
    sleep(4)
    print("I've pulled you out of there. Don't worry about your 'allies', they are probably fine. Maybe. Anyway, I've teleported you somewhere new.")
    sleep(4)
    print("Time for a new chapter. Let's call it...")
    sleep(3)
    game_state['current_location'] = 'trimbolton'
    save_game()

def trimbolton_hub():
    global game_state
    game_state['current_location'] = 'trimbolton'
    print("\n\n--- ACT 3: War without reason ---\n")
    sleep(3)
    print("You awaken to the smell of coal smoke and hot metal, and the constant sound of whirring gears and hissing pistons. You are in Trimbolton, a sprawling city of brass, copper, and steam.")
    sleep(4)
    print("Towering clockwork structures pierce the perpetually hazy sky, and automatons walk the streets alongside people in leather aprons and brass goggles. This is a city built on invention and industry.")
    sleep(4)
    while True:
        print("\n--- Trimbolton Town Square ---")
        choice = get_player_input("""What would you like to do?
1. Visit the Grand Cogsmith to admire new inventions.
2. Challenge the infamous Steam-Powered Pirate at the docks.
3. Inquire at the Automaton Information Hub.
4. Browse the wares at the Brass Goggle Emporium.
5. Investigate the abandoned gear-works on the edge of town.
6. Challenge the star of the Steam-powered Stage: Mettaton!
7. Talk to the Airship Captains about the world beyond.
8. Sample the local 'Oil-Stout' at 'The Rusty Cog' tavern.
9. Observe the great clock in the town center and its complex mechanisms.
10. Save and Quit
11. Customize Moveset
Choice: """, valid_choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        print()
        sleep(1)
        if choice == 1:
            print("You visit the Grand Cogsmith, a master inventor. He shows you a self-peeling potato and a device that butters toast on both sides. You are moderately impressed.")
        elif choice == 2:
            print("You head to the docks and find Captain 'Cog-Eye' Pete, a pirate whose body is more machine than man. He scoffs at you.")
            print("'You think you have what it takes to face me, landlubber?' He revs a chainsaw built into his arm. 'Let's see!'")
            battle_sequence(
                enemy_type="steampunk_pirate",
                win_hp_bonus=10,
                death_hp_reset=game_state['player_max_hp'],
            )
        elif choice == 3:
            print("An automaton at the hub provides you with a perfectly printed map of the city and the current time, down to the millisecond. It's very efficient.")
        elif choice == 4:
            print("The Emporium is full of strange and wonderful goggles. Some for seeing in the dark, some for seeing very small things, and some that are just for fashion. You decide your current look is fine.")
        elif choice == 5:
            print("You explore the abandoned gear-works. It's spooky and filled with cobwebs (and gearwebs). You find a small, perfectly balanced cog and pocket it for good luck.")
        elif choice == 6:
            print("You enter a grand theater where a dazzling, boxy robot is performing to a sold-out crowd. This is Mettaton.")
            print("METTATON: 'OH, A CHALLENGER? DOES THIS NEW FACE HAVE THE... RATINGS TO FACE ME? LET'S FIND OUT, DARLING!'")
            result = battle_sequence(
                enemy_type="mettaton",
                win_hp_bonus=25,
                death_hp_reset=game_state['player_max_hp'],
            )
            if result == "win":
                print("\nMETTATON: 'OH MY! WHAT A PERFORMANCE! YOU'VE TRULY... STOLEN THE SHOW!'")
                sleep(2)
                print("As Mettaton explodes in a shower of confetti, a piece of sophisticated armor is left behind.")
                if not game_state['has_firefly_armor']:
                    game_state['has_firefly_armor'] = True
                    print("\nYou have acquired the **Firefly Armor**! This advanced piece of tech has a chance to retaliate against attackers with a voltaic burst!")
                else:
                    print("You already have the Firefly Armor, but the applause is a nice reward!")
                sleep(3)
                game_state['current_location'] = 'sea_voyage'
                save_game()
                return
        elif choice == 7:
            print("The airship captains tell tales of floating islands and cities in the sky. It seems the world is much bigger than you thought.")
        elif choice == 8:
            print("You try the 'Oil-Stout'. It's... thick. And metallic. You feel... lubricated? You gain 5 HP.")
            game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + 5)
        elif choice == 9:
            print("You watch the great clock for an hour. Its movements are mesmerizing. You feel centered and focused. (+10 Focus)")
            game_state['focus'] = min(game_state['max_focus'], game_state['focus'] + 10)
        elif choice == 10:
            save_game()
            game_state['current_location'] = 'quit'
            return
        elif choice == 11:
            customize_moveset()
        sleep(3)

def start_sea_voyage():
    global game_state
    game_state['current_location'] = 'sea_voyage'
    print("\nWith Mettaton defeated and the crowd in an uproar, you know you can't stay. The authorities of Trimbolton will be here any minute.")
    sleep(3)
    print("You slip out the back of the theater and make a break for the docks, the sounds of chaos fading behind you.")
    sleep(3)
    print("You hide out at a resource docking bay, the air thick with the smell of brine and machine oil. You spot a small, forgotten dinghy tied to a post. Next to it, a waterproof satchel containing a map.")
    sleep(4)
    print("It's a risky move, but it's your only one. Under the cloak of the industrial haze, you untie the dinghy and push off into the open sea. Your destination, according to the map: Ebott Bay.")
    sleep(4)
    days_at_sea = 0
    while True:
        days_at_sea += 1
        monsters_defeated = game_state['gash_defeated'] and game_state['harpoon_defeated']
        if days_at_sea > 4 and monsters_defeated:
            print("\nAfter what feels like an eternity at sea, you spot a coastline matching the map's description. You've made it.")
            sleep(3)
            game_state['current_location'] = 'ebott_bay'
            save_game()
            break
        print("\n--- On the Open Sea ---")
        print("The waves rock your small boat. The map shows the general direction of Ebott Bay, but the journey is fraught with peril.")
        choices = {}
        if not game_state['harpoon_defeated']: choices[1] = "Follow a beautiful, distant melody."
        if not game_state['gash_defeated']: choices[2] = "Sail towards a shadowy figure under the waves."
        if not game_state['tsunami_swiper_unlocked']: choices[3] = "Investigate a glimmer in the water (Unlock Tsunami Swiper)."
        choices[4] = "Sail onward towards Ebott Bay."
        choices[5] = "Fish for supplies."
        choices[6] = "Save Game and Quit"
        choices[7] = "Customize Moveset"
        prompt_text = "What will you do?\n"
        for num, text in choices.items():
            prompt_text += f"{num}. {text}\n"
        prompt_text += "Choice: "
        voyage_choice = get_player_input(prompt_text, valid_choices=list(choices.keys()))
        print()
        sleep(1)
        if voyage_choice == 1 and not game_state['harpoon_defeated']:
            print("The beautiful song grows louder, enchanting your senses. You sail towards a rocky outcrop where a figure sits. As you draw closer, you see it's a woman with the tail of a fish, and one of her arms is a wickedly sharp, bony spear.")
            print("'Another sailor, drawn to my song?' she whispers, her voice like honey and venom. 'You'll make a fine trophy!'")
            result = battle_sequence(
                enemy_type="harpoon",
                win_hp_bonus=15,
                death_hp_reset=game_state['player_max_hp'],
            )
            if result == "win":
                game_state['harpoon_defeated'] = True
        elif voyage_choice == 2 and not game_state['gash_defeated']:
            print("The large, dark shape beneath your boat begins to circle. It moves with an unnatural speed. Suddenly, a spectral fin slices the water's surface as a phantom shark lunges!")
            result = battle_sequence(
                enemy_type="gash",
                win_hp_bonus=15,
                death_hp_reset=game_state['player_max_hp'],
            )
            if result == "win":
                game_state['gash_defeated'] = True
        elif voyage_choice == 3 and not game_state['tsunami_swiper_unlocked']:
            print("You steer the dinghy towards a faint, pulsing light just beneath the surface. You'll need to reach into the water to get it.")
            print("This requires a steady hand. Let's see how focused you are.")
            sleep(2)
            if game_state['focus'] >= 40:
                print("Your focus is sharp. You carefully reach into the cold water, your hand closing around a waterlogged, leather-bound book. The runes on it glow faintly.")
                print("\nYou've found a Spellbook! You learn a new special move: Tsunami Swiper!")
                game_state['tsunami_swiper_unlocked'] = True
                game_state['focus'] -= 10
            else:
                print("You try to grab the object, but your focus wavers. A strong current pulls it just out of your reach, and it sinks into the abyss.")
                print("The opportunity is lost for now.")
        elif voyage_choice == 4:
            print("You sail onward, keeping the map's direction in mind. The sun beats down and the sea is calm for now.")
            if random.random() < 0.2:
                print("A storm brews on the horizon. You expertly navigate the rough waves and continue on, exhausted but safe.")
                game_state['focus'] = max(0, game_state['focus'] - 10)
                print(f"The effort cost you some focus. Current Focus: {game_state['focus']}")
        elif voyage_choice == 5:
            print("You cast a small net, hoping for a meal. You manage to catch a few fish.")
            heal_amt = random.randint(10, 20)
            game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + heal_amt)
            print(f"You eat the fresh fish and feel revitalized. You heal for {heal_amt} HP. Current Health: {game_state['hp']}/{game_state['player_max_hp']}")
        elif voyage_choice == 6:
            save_game()
            game_state['current_location'] = 'quit'
            return
        elif voyage_choice == 7:
            customize_moveset()
        sleep(2)

def leat_boss_fight():
    phase = 1
    leat_hp = ALL_ENEMY_STATS['leat']['hp']
    leat_max_hp_p2 = 600
    leat_shadow_stepped = False
    leat_is_charging = False
    game_state['hp'] = game_state['player_max_hp']
    game_state['charge'] = 0
    game_state['focus'] = game_state['max_focus'] // 2
    game_state['crit_next_turn'] = False
    game_state['enemy_stunned'] = False
    game_state['enemy_damage_multiplier'] = 1.0
    game_state['overdrive_active'] = False
    game_state['overdrive_turns_left'] = 0
    game_state['rebound_barrage_active'] = False
    game_state['rebound_barrage_turns'] = 0
    game_state['rebound_barrage_remaining_dmg'] = 0
    game_state['bleed_next_turn'] = False
    print("\n--- BOSS FIGHT: LEAT, THE SILENT BLADE ---")
    while leat_hp > 0 and game_state['hp'] > 0:
        action_taken_this_turn = False
        while not action_taken_this_turn:
            leat_phase_name = "Leat" if phase == 1 else "Leat (Solemn Lament)"
            print(f"\n--- Your Turn ({leat_phase_name}: {leat_hp} HP | You: {game_state['hp']}/{game_state['player_max_hp']} HP | Charge: {game_state['charge']}% | Focus: {game_state['focus']}/{game_state['max_focus']}) ---")
            if leat_is_charging:
                print("\nLeat is gathering immense power for a SOLEMN REQUIEM! You must defend!")
            player_choice = get_player_input("""What shall you do?
1. Attack
2. Special Moves
3. Defend
4. Use Ultimate
5. Change Stance
Choice: """, valid_choices=[1, 2, 3, 4, 5])
            print()
            sleep(1)
            if player_choice == 1:
                if leat_shadow_stepped:
                    if random.random() < 0.5:
                        print("Leat sidesteps your attack with impossible speed! Your blow hits nothing but air!")
                        action_taken_this_turn = True
                        leat_shadow_stepped = False
                        break
                    else:
                        print("You manage to track her movements and land a hit through her shadow form!")
                        leat_shadow_stepped = False
                print("Your available attacks:")
                valid_attack_choices = []
                for i, attack_name in enumerate(game_state['player_attack_moveset']):
                    attack_data = ALL_PLAYER_ATTACKS[attack_name]
                    print(f"{i+1}. {attack_data['name']} (Cost: {attack_data['focus_cost']} Focus) - {attack_data['desc']}")
                    valid_attack_choices.append(i + 1)
                attack_index = get_player_input("Choose your attack: ", valid_choices=valid_attack_choices) - 1
                chosen_attack_name = game_state['player_attack_moveset'][attack_index]
                leat_hp, action_taken_this_turn = attack_enemy("Leat", leat_hp, ALL_ENEMY_STATS['leat']['ret_dmg_range'])
            elif player_choice == 2:
                print("Your available special moves:")
                valid_special_choices = []
                for i, attack_name in enumerate(game_state['player_special_moveset']):
                    attack_data = ALL_PLAYER_ATTACKS[attack_name]
                    print(f"{i+1}. {attack_data['name']} (Cost: {attack_data['focus_cost']} Focus) - {attack_data['desc']}")
                    valid_special_choices.append(i + 1)
                attack_index = get_player_input("Choose your special move: ", valid_choices=valid_special_choices) - 1
                chosen_attack_name = game_state['player_special_moveset'][attack_index]
                leat_hp, action_taken_this_turn = attack_enemy("Leat", leat_hp, ALL_ENEMY_STATS['leat']['ret_dmg_range'])
            elif player_choice == 3:
                defense_choice = get_player_input("""Choose your defense:
1. Parry (High risk, high reward)
2. Focus Charge (Take damage, gain Focus)
Choice: """, valid_choices=[1, 2])
                if defense_choice == 1:
                    action_taken_this_turn = defend("Leat", "parry", ALL_ENEMY_STATS['leat']['ret_dmg_range'])
                elif defense_choice == 2:
                    action_taken_this_turn = defend("Leat", "focus_charge", ALL_ENEMY_STATS['leat']['ret_dmg_range'])
            elif player_choice == 4:
                leat_hp, action_taken_this_turn = use_ult("Leat", leat_hp)
            elif player_choice == 5:
                change_player_stance()
                action_taken_this_turn = True
        if leat_hp <= 0 and phase == 1:
            phase = 2
            leat_hp = leat_max_hp_p2
            print("\nLeat stumbles back, clutching a wound in her side. She grits her teeth.")
            sleep(2)
            print("'You're... strong,' she pants. 'Stronger than the others.'")
            sleep(3)
            print("She holds her bone dagger aloft, its surface beginning to weep a black, oily substance. A mournful cry echoes from the blade itself.")
            sleep(4)
            print("'But you haven't faced my sorrow! Cry with me, SOLEMN LAMENT!'")
            sleep(2)
            print("\n--- PHASE 2: SOLEMN LAMENT ---")
            game_state['enemy_stunned'] = False
            continue
        if leat_hp <= 0:
            break
        print("\n--- Leat's Turn ---")
        sleep(1)
        if game_state['enemy_stunned']:
            print("Leat is stunned and cannot act!")
            game_state['enemy_stunned'] = False
            continue
        if leat_is_charging:
            print("Leat unleashes her charged energy!")
            requiem_dmg = random.randint(80, 120)
            if game_state['stance'] == 'defensive':
                requiem_dmg = int(requiem_dmg * 0.5)
                print("Your defensive stance significantly reduced the impact!")
            game_state['hp'] -= requiem_dmg
            print(f"The SOLEMN REQUIEM explodes, dealing a massive {requiem_dmg} damage! Your HP: {game_state['hp']}")
            leat_is_charging = False
        elif phase == 1:
            dmg = random.randint(20, 35)
            game_state['hp'] -= dmg
            print(f"Leat strikes with a series of blindingly fast jabs, dealing {dmg} damage! Your HP: {game_state['hp']}")
        elif phase == 2:
            attack_choice = random.choice(['echoing_blade', 'shadow_step', 'vitae_drain', 'solemn_requiem'])
            if attack_choice == 'echoing_blade':
                dmg = random.randint(30, 45)
                game_state['hp'] -= dmg
                print(f"Leat's Echoing Blade slashes you for {dmg} damage! Your HP: {game_state['hp']}")
            elif attack_choice == 'shadow_step':
                dmg = random.randint(15, 25)
                game_state['hp'] -= dmg
                leat_shadow_stepped = True
                print(f"Leat dissolves into shadow, striking you for {dmg} damage before reappearing! She will be hard to hit next turn. Your HP: {game_state['hp']}")
            elif attack_choice == 'vitae_drain':
                dmg = random.randint(20, 30)
                heal = int(dmg * 0.75)
                game_state['hp'] -= dmg
                leat_hp = min(leat_max_hp_p2, leat_hp + heal)
                print(f"Leat performs a Vitae Drain, dealing {dmg} damage and healing herself for {heal} HP! Your HP: {game_state['hp']}")
            elif attack_choice == 'solemn_requiem':
                leat_is_charging = True
                print("Leat stabs her dagger into the ground. Dark energy begins to coalesce around her. She's preparing a devastating attack!")
        sleep(2)
        if game_state['hp'] <= 0:
            print("\nYou have been defeated by Leat's relentless assault. As your vision fades, you hear her quiet apology...")
            sleep(2)
            return "lose"
    if game_state['hp'] > 0:
        print("\nWith a final, desperate strike, you break through Leat's guard. Her dagger, Solemn Lament, shatters into a thousand pieces of dark crystal.")
        sleep(3)
        print("She falls to her knees, defeated. 'It is done... I am free from the lament.'")
        sleep(2)
        game_state['leat_defeated'] = True
        award_exp(ALL_ENEMY_STATS['leat']['exp_reward'])
        game_state['hp'] = game_state['player_max_hp']
        return "win"

def act_4_ebott_bay():
    global game_state
    game_state['current_location'] = 'ebott_bay'
    if game_state['leat_defeated']:
        print("\nYou stand on the shores of Ebott Bay, the shattered remains of Solemn Lament a reminder of your battle. The war has been brought to you, but you survived the first assault.")
        game_state['current_location'] = 'post_leat_camp'
        return
    print("\nYou pull your dinghy ashore onto the sands of Ebott Bay. The air is different here... heavy with an unspoken history.")
    sleep(3)
    print("Welcome to Ebott Bay. The looming mountain casts a long shadow over the quiet coastal town.")
    sleep(3)
    print("\n*BZZT*... A crackle comes from a small radio you salvaged from the dinghy. It sputters to life.")
    sleep(3)
    print("\nVOICE (Angstrom Levy): '...can you hear me? I know you can. We know where you are.'")
    sleep(4)
    print("\nVOICE (Angstrom Levy): 'Listen. What happened with Grimm... it was a demonstration. The Regents' offer was too good to refuse. We have our orders.'")
    sleep(4)
    print("\nVOICE (Angstrom Levy): 'You were always the unpredictable one. The variable that couldn't be controlled. And for that, you must be eliminated. Consider our alliance... formally dissolved. This is war now.'")
    sleep(4)
    print("\nThe radio cuts to static. Before you can even process the betrayal, you hear a sharp *thwip* sound.")
    sleep(2)
    print("A wicked-looking bone dagger is embedded in the sand just inches from your foot.")
    sleep(3)
    print("From the shadows of the cliffs, a figure drops to the ground with silent grace. It's Leat. Her expression is grim, her movements fluid and ready.")
    sleep(4)
    print("\nLEAT: 'Nothing personal. I'm just following orders.'")
    sleep(2)
    while True:
        result = leat_boss_fight()
        if result == "win":
            break
        else:
            retry_choice = get_player_input("\nDefeated. The fight was too much. \n1. Try Again \n2. Load last save\nChoice: ", [1, 2])
            if retry_choice == 1:
                print("You steel your will and prepare to face Leat once more.")
                continue
            else:
                game_state['current_location'] = 'quit'
                return
    print("\nYou look down at the defeated Leat, then towards the horizon. One down, three to go. This war is just beginning.")
    sleep(3)
    game_state['current_location'] = 'post_leat_camp'
    save_game()

def post_leat_camp_hub():
    global game_state
    game_state['current_location'] = 'post_leat_camp'
    print("\n--- Ebott Bay Camp ---")
    print("You make a small camp on the beach to recover from your fight. The mountain looms over you, a silent giant.")
    print("You know the others will come for you eventually. You need to prepare.")
    sleep(3)
    print("\nYou set up camp and begin travelling towards the town of Ebott proper.")
    sleep(3)
    print("During the journey, you notice your sword, Lobos, isn't looking the same. The ethereal glow seems to flicker erratically.")
    sleep(4)
    print("The dark energy from Leat's shattered dagger must have mixed with it, causing their essences to conflict...")
    sleep(4)
    game_state['current_location'] = 'ebott_town_hub'
    save_game()

def ebott_town_hub():
    global game_state
    game_state['current_location'] = 'ebott_town_hub'
    print("\n--- Ebott Town ---")
    print("You find a small, secluded room to rent and lie low. The town is quiet, but you can feel the tension in the air.")
    print("You need to gather information on the Monarchs and your former allies.")
    sleep(3)
    while True:
        choice = get_player_input("""
What is your next move?
1. Listen to radio chatter for Monarch transmissions.
2. Exchange information with shady contacts at the docks.
3. Check on Lobos.
4. Prepare for an ambush.
5. Save and Quit.
6. Customize Moveset.
Choice: """, [1, 2, 3, 4, 5, 6])
        print()
        sleep(1)
        if choice == 1:
            print("You spend hours fiddling with the radio. Amidst the static, you hear coded messages about troop movements and supply routes. It seems the Monarchs are mobilizing for a larger conflict.")
        elif choice == 2:
            print("You meet a cloaked figure at the docks who, for a small price, tells you about your former allies. Angstrom is coordinating things from a distance. Grimm is nowhere to be seen. Graystone, however, has been asking questions around town...")
        elif choice == 3:
            print("You draw Lobos. The blade feels unstable, its light pulsing violently between silver-blue and a venomous purple. It's clear the weapon is fighting itself, on the verge of shattering.")
        elif choice == 4:
            print("You know they're coming. You find a defensible position in an old quarry outside town and wait.")
            sleep(3)
            print("The ground trembles. A colossal figure blocks the entrance to the quarry.")
            sleep(2)
            print("GRAYSTONE: 'I was told to eliminate you. But I am a warrior, not an assassin. Face me with honor!'")
            sleep(3)
            graystone_boss_fight()
            if game_state.get('graystone_defeated', False):
                return
        elif choice == 5:
            save_game()
            game_state['current_location'] = 'quit'
            return
        elif choice == 6:
            customize_moveset()
        sleep(2)

def graystone_boss_fight():
    print("\n--- BOSS FIGHT: GRAYSTONE ---")
    result = battle_sequence(
        enemy_type="graystone",
        win_hp_bonus=50,
        death_hp_reset=game_state['player_max_hp']
    )
    if result == "win":
        print("\nGraystone falls to one knee, his stone armor cracking. 'Impressive... you are a true warrior.'")
        sleep(3)
        print("He begins to glow with an intense energy. 'BUT THIS IS MY FINAL DUTY!'")
        sleep(2)
        print("He lunges forward for a last-ditch attack! You raise Lobos to defend!")
        sleep(2)
        print("\nThere is a blinding flash of light and a sound like shattering crystal.")
        sleep(3)
        print("Graystone collapses, defeated. But Lobos... is gone. The blade has been utterly destroyed in the impact.")
        sleep(4)
        print("In its place, a swirling mass of silver liquid hangs in the air. The spirit of Lobos, broken and enraged, lashes out.")
        sleep(4)
        print("The liquid silver flies towards you, engulfing your hands and forearms. The pain is immense, but you feel a new, raw power coursing through you.")
        sleep(5)
        print("\nThe silver solidifies into a pair of ornate, glowing gauntlets.")
        print("\n--- You have acquired the **Beowulf** Gauntlets! ---")
        sleep(3)
        game_state['has_lobos_sword'] = False
        game_state['lobos_power_unlocked'] = False
        game_state['has_beowulf_gauntlets'] = True
        game_state['graystone_defeated'] = True
        game_state['current_weapon'] = 'gauntlets'
        print("Your fighting style has completely changed! You must customize your moveset to reflect your new capabilities with hand-to-hand combat.")
        sleep(4)
        customize_moveset()
        game_state['current_location'] = 'abandoned_outpost'
        save_game()
    else:
        print("You were overwhelmed by Graystone's power. You must retreat and prepare.")

def abandoned_outpost_hub():
    global game_state
    game_state['current_location'] = 'abandoned_outpost'
    print("\nYou are compromised. With Graystone defeated, you flee into the wilderness, the new weight on your hands a constant reminder of your loss... and your new power.")
    sleep(4)
    print("You eventually reach an abandoned forest outpost. It's not much, but it's shelter. It's a place to think.")
    sleep(3)
    print("Rummaging through a dusty desk, you find a leather-bound journal and a pen that still works. A place to record your thoughts. A diary.")
    sleep(4)
    print("\n--- DIARY UNLOCKED ---")
    print("You can now access your diary from most hubs to read or write entries.")
    sleep(3)
    print("\nYou sit down and write your first message, the words flowing onto the page...")
    game_state['diary_entries'].append("Lobos is gone. Graystone is defeated. These gauntlets... they feel different. Heavier. Angrier. Two down. Two to go. Angstrom, I'm coming for you.")
    print("First diary entry recorded.")
    save_game()
    sleep(3)
    print("\nLater, you tinker with the radio, patching it into the outpost's old antenna. It crackles to life, and a familiar, smug voice fills the room.")
    sleep(4)
    print("ANGSTROM: 'I felt that. The resonance of a collapsing nexus. Graystone. Impressive. You truly are full of surprises.'")
    sleep(4)
    print("You grab the microphone. 'Angstrom! Your turn is coming. Once I find you, I will personally bash you down!'")
    sleep(4)
    print("A dry chuckle from the radio. 'Such passion! Such fury! It will make your eventual failure all the more delicious. I'm not a brute like Graystone, little hero. You can't punch your way through reality itself. But please, do try.'")
    sleep(5)
    print("The radio goes silent. You clench your new gauntlets. The journey is not over.")
    sleep(3)
    print("\nAs you prepare to leave, you notice the gauntlets glowing softly. Two voices, a harmonious chord, echo in your mind, much like Lobos used to, but different.")
    sleep(4)
    print("VOICE 1 (Bright and Sharp): 'We are born of his sacrifice. His will, reforged.'")
    sleep(4)
    print("VOICE 2 (Calm and Deep): 'He was one. We are two. A new balance. A new power.'")
    sleep(4)
    print("VOICE 1: 'I am Soleil. The fury of the sun. The relentless attack.'")
    sleep(4)
    print("VOICE 2: 'I am Lune. The certainty of the moon. The patient defense.'")
    sleep(4)
    print("\n--- NEW STANCES UNLOCKED ---")
    print("Soleil Stance replaces Offensive. Lune Stance replaces Defensive. Each grants a powerful new special move, usable only in that stance.")
    sleep(4)
    game_state['current_location'] = 'gardina'
    save_game()

def gardina_hub():
    global game_state
    game_state['current_location'] = 'gardina'
    print("\nFollowing a new lead, you arrive at the city of **Gardina**.")
    sleep(3)
    print("The city is carved from a massive, jade-like mountain. Buildings spiral upwards, glowing with a soft green light. The people are serene, adorned with jade jewelry, and move with a quiet purpose. These are the Jade Worshippers.")
    sleep(5)

    while True:
        print("\n--- Gardina Plaza ---")
        prompt = """The city of Jade awaits. What will you do?
1. Meditate at the Great Jade Shrine.
2. Observe the Jade Artisans at work.
3. Challenge a Jade Golem in the sparring circle.
4. Speak to a Worshipper Acolyte.
5. Play a game of 'Jade Stones'.
6. Purchase a blessed Jade Charm.
7. Investigate the 'Whispering Vein'.
8. Help a miner with a pest problem.
9. Look through your Diary.
10. Find a quiet spot and listen to the radio...
Choice: """
        choice = get_player_input(prompt, list(range(1, 11)))
        print()
        sleep(1)

        if choice == 1:
            print("You sit before the giant, glowing heart of the city. The serene energy calms your mind. (+15 Focus)")
            game_state['focus'] = min(game_state['max_focus'], game_state['focus'] + 15)
        elif choice == 2:
            print("You watch artisans carve intricate patterns into pieces of jade. Their precision is mesmerizing. You feel you've learned something about finding weak points. (Next critical hit deals +25% damage)")
        elif choice == 3:
            battle_sequence("jade_golem", win_hp_bonus=10, death_hp_reset=game_state['player_max_hp'])
        elif choice == 4:
            print("The acolyte speaks of the 'Great Cycle' and the 'Stone's Embrace'. You get the sense that they view life and death as part of a larger, beautiful pattern. It's strangely comforting.")
        elif choice == 5:
            print("You play a complex strategy game involving placing jade stones on a grid. You lose spectacularly, but the mental exercise is invigorating.")
        elif choice == 6:
            print("You buy a small, polished jade charm. It feels warm to the touch. It seems to bolster your vitality. (+10 Max HP)")
            game_state['player_max_hp'] += 10
            game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + 10)
            print(f"Your Max HP is now {game_state['player_max_hp']}!")
        elif choice == 7:
            print("You follow rumors of a 'Whispering Vein' deep in the mines. You find a vein of raw jade that seems to hum with energy, but it's too deep to excavate without proper tools.")
        elif choice == 8:
            print("A miner complains of giant crystal-crabs in his shaft. You agree to help.")
            battle_sequence("skeleton", win_hp_bonus=5, intro_text="You fight a Giant Crystal-Crab (reskinned skeleton)!")
            print("The miner thanks you with a handful of valuable gems.")
        elif choice == 9:
            manage_diary()
        elif choice == 10:
            print("You find a high balcony overlooking the city, setting up your radio. You tune the dials, listening for anything...")
            sleep(4)
            print("Static. Nothing but static. You're about to give up when a voice crackles through, loud and clear, seemingly right beside you.")
            sleep(3)
            print("\nANGSTROM: 'Above you.'")
            sleep(2)
            print("You look up just as a figure drops from a shimmering portal, landing silently on the balcony railing. It's Angstrom Levy.")
            sleep(3)
            print("ANGSTROM: 'No more running. Let's finish this.'")
            sleep(2)
            angstrom_boss_fight()
            return

def angstrom_boss_fight():
    print("This will be the boss fight with Angstrom. Story to be continued!")
    game_state['angstrom_defeated'] = True
    game_state['current_location'] = 'act_4_opening'
    save_game()

def act_4_opening_cutscene():
    global game_state
    game_state['current_location'] = 'act_4_opening'
    print("\n\n--- ACT 4: THE LOWEST RUNG ---\n")
    sleep(3)
    print("*** CUTSCENE: The Regent's Council ***")
    sleep(2)
    print("In the grand hall, Grand Regent Thragg stares at a holographic display showing three names, all crossed out in red: LEAT, GRAYSTONE, ANGSTROM LEVY.")
    sleep(5)
    print("\nWEEP: (sobbing) 'They're gone... all gone... That variable... it consumed them...'")
    sleep(4)
    print("\nVERGIL: 'The asset has exceeded all projections. Its growth rate is... anomalous.'")
    sleep(4)
    print("\nGRAND REGENT THRAGG: 'They were a test. A filter. And they failed.'")
    sleep(4)
    print("Thragg gestures, and the list of 'elite threats' expands. Below the crossed-out names are dozens more, each one more terrifying and alien than the last.")
    sleep(5)
    print("\nGRAND REGENT THRAGG: 'You all seem to forget. The traitors... the hero... they were at the bottom of the list. The lowest rung. They were nothing.'")
    sleep(5)
    print("\nGRAND REGENT THRAGG: 'Now, the real powers have taken notice. The ones who feast on worlds and shatter stars. They know the asset's name. And they are coming.'")
    sleep(5)
    print("\nGRAND REGENT THRAGG: 'Let them come. Let them break our little hero for us.'")
    sleep(3)
    print("\n*** END CUTSCENE ***")
    sleep(4)
    game_state['current_location'] = 'fork_in_the_road'
    save_game()

def fork_in_the_road_hub():
    global game_state
    game_state['current_location'] = 'fork_in_the_road'
    print("\nYou leave the city of Gardina behind, the Regent's words from some unknown broadcast echoing in your mind. A bigger threat is coming.")
    sleep(4)
    print("Your journey takes you to a literal fork in the road. One path leads up a volcanic, fiery mountain. The other descends into a misty, deep-sea trench, somehow accessible from the mainland.")
    sleep(5)
    print("\nThe voices of your gauntlets speak to you.")
    sleep(2)
    print("SOLEIL: 'The path of fire! Of passion! There we can temper our rage into a dragon's inferno! This is the Fernit path!'")
    sleep(4)
    print("LUNE: 'The path of the abyss. Of secrets. There we can shape our will into the crushing pressure of the depths. This is the Taph path.'")
    sleep(4)
    
    while 'beowulf_style' not in game_state or game_state['beowulf_style'] is None:
        choice = get_player_input("""You must choose a path to master your new power. This choice is permanent.
1. Ascend the Volcano. (Choose the Dragon Style of Fernit)
2. Descend into the Trench. (Choose the Leviathan Style of Taph)
Choice: """, [1, 2])
        if choice == 1:
            print("You choose the path of flame. Your gauntlets glow with the heat of a forge.")
            game_state['beowulf_style'] = 'fernit'
            game_state['current_location'] = 'fernit_path'
        elif choice == 2:
            print("You choose the path of the abyss. Your gauntlets feel heavy, like the crushing deep.")
            game_state['beowulf_style'] = 'taph'
            game_state['current_location'] = 'taph_path'
        save_game()

def fernit_path_hub():
    global game_state
    game_state['current_location'] = 'fernit_path'
    print("\nYou arrive at the Ashen Hold of Fernit, a town built into the caldera of a dormant volcano. The air is warm, and smoke rises from countless forges.")
    while True:
        choice = get_player_input("""What will you do in the Ashen Hold?
1. Visit the Obsidian Forge.
2. Temper your gauntlets in a lava stream.
3. Speak to the Elder Wyrm-Speaker.
4. Challenge a Magma Golem.
5. Hunt a pack of Ash Hounds.
6. Rest by the Heart-Stone.
7. Climb to the summit of the volcano.
Choice: """, list(range(1, 8)))
        
        if choice == 1:
            print("Blacksmiths here use magma to shape obsidian into weapons. They offer to sharpen your gauntlets' edges, granting a temporary damage boost.")
        elif choice == 2:
            print("You hold your gauntlets over a flowing river of lava. The heat is immense. It's a test of will, and you pass, feeling your bond with Soleil strengthen.")
        elif choice == 3:
            print("The Elder speaks of the dragon spirit: 'It is not just fire, but the will to dominate. To be the apex. Do not let it consume you.'")
        elif choice == 4:
            battle_sequence("magma_golem")
        elif choice == 5:
            battle_sequence("ash_hound")
        elif choice == 6:
            print("You rest by a large, warm stone at the town's center. You feel rejuvenated.")
            game_state['hp'] = game_state['player_max_hp']
            game_state['focus'] = game_state['max_focus']
        elif choice == 7:
            print("Your training is complete. You ascend to the volcano's peak, ready for what's next.")
            cifer_boss_fight()
            return

def taph_path_hub():
    global game_state
    game_state['current_location'] = 'taph_path'
    print("\nYou descend into the Abyssal City of Taph, a metropolis of bioluminescent coral built within a colossal underwater cave. The water pressure is immense, but a strange magic lets you breathe.")
    while True:
        choice = get_player_input("""What will you do in the Abyssal City?
1. Explore the Bioluminescent Coral Gardens.
2. Navigate the Labyrinthine Trench.
3. Listen to the whispers of the Deep Sage.
4. Subdue a Trench Kraken.
5. Disperse a school of Abyssal Sharks.
6. Meditate in a quiet pressure-vent cave.
7. Descend to the Trench Floor.
Choice: """, list(range(1, 8)))

        if choice == 1:
            print("You walk through gardens of glowing coral. The strange, silent beauty of the deep is both calming and unsettling.")
        elif choice == 2:
            print("You enter a maze of deep-sea tunnels. After several wrong turns, you find a hidden chamber with a chest containing ancient coins.")
        elif choice == 3:
            print("The Deep Sage, a being of pure water and light, whispers: 'The abyss is not empty. It is patient. It crushes all who are impatient. Learn from it.'")
        elif choice == 4:
            battle_sequence("trench_kraken")
        elif choice == 5:
            battle_sequence("abyssal_shark")
        elif choice == 6:
            print("You find a cave where warm water vents from the planet's core. You feel your energy returning.")
            game_state['hp'] = game_state['player_max_hp']
            game_state['focus'] = game_state['max_focus']
        elif choice == 7:
            print("Your training is complete. You swim to the deepest part of the trench, ready for what's next.")
            cifer_boss_fight()
            return

def cifer_boss_fight():
    # --- Phase 1 Data ---
    phase = 1
    cifer_hp = ALL_ENEMY_STATS['cifer']['hp']
    cifer_name = "Cifer"

    # --- Phase 2 Data ---
    cifer_p2_max_hp = 4500
    
    # --- Battle Setup ---
    game_state['hp'] = game_state['player_max_hp']
    start_charge = 25 if game_state.get('player_clan') == 'tojo' else 0
    game_state['charge'] = start_charge
    game_state['focus'] = game_state['max_focus']
    game_state['crit_next_turn'] = False
    game_state['enemy_stunned'] = False
    game_state['enemy_damage_multiplier'] = 1.0
    
    print("\nAs you reach the end of your path, the blank, hollow being, Cifer, appears before you.")
    sleep(3)
    path_style = game_state.get('beowulf_style', 'path')
    if path_style == 'fernit':
        print("<< The Dragon's fire. Predictable. >>")
    else:
        print("<< The Leviathan's pressure. A futile effort. >>")
    sleep(4)
    print("<< You seek mastery, but you only understand a fraction of true power. The spirits within me will demonstrate. >>")
    sleep(4)
    
    print(f"\n--- BOSS FIGHT: {cifer_name.upper()} ---")

    while cifer_hp > 0 and game_state['hp'] > 0:
        # --- Player Turn ---
        action_taken_this_turn = False
        while not action_taken_this_turn:
            print(f"\n--- Your Turn ({cifer_name}: {cifer_hp} HP | You: {game_state['hp']}/{game_state['player_max_hp']} HP | Charge: {game_state['charge']}% | Focus: {game_state['focus']}/{game_state['max_focus']}) ---")
            player_choice = get_player_input("1. Attack\n2. Special Moves\n3. Defend\n4. Use Ultimate\n5. Change Stance\nChoice: ", [1, 2, 3, 4, 5])
            print()
            if player_choice == 1:
                # Attack logic... (shortened for brevity)
                attack_index = get_player_input("Choose your attack: ", [i+1 for i, _ in enumerate(game_state['player_attack_moveset'])]) - 1
                chosen_attack_name = game_state['player_attack_moveset'][attack_index]
                cifer_hp, action_taken_this_turn = attack_enemy(cifer_name, cifer_hp, (35, 50))
            elif player_choice in [2, 3, 4, 5]:
                # Placeholder for other actions
                print("Handling other actions...")
                # ... (full implementation of other actions would go here)
                action_taken_this_turn = True # Simplified for this example
            if not action_taken_this_turn: print("Action failed. Try again.")

        # --- Phase Transition ---
        if cifer_hp <= 0 and phase == 1:
            phase = 2
            cifer_hp = cifer_p2_max_hp
            cifer_name = "Cifer (Dark Rising)"
            print("\nCifer's form shatters, but a malevolent spirit erupts from the remains, reshaping the dust into a larger, more terrifying figure.")
            sleep(3)
            print("<< TRUE POWER IS NOT WIELDED. IT IS UNLEASHED! >>")
            sleep(2)
            print(f"\n--- {cifer_name.upper()} ---")
            continue

        if cifer_hp <= 0: break # End fight if phase 2 is defeated

        # --- Cifer's Turn ---
        print(f"\n--- {cifer_name}'s Turn ---")
        if game_state['enemy_stunned']:
            print(f"{cifer_name} is stunned!")
            game_state['enemy_stunned'] = False
            continue

        if phase == 1:
            attack = random.choice(['void_slash', 'spirit_lance', 'hollow_gaze', 'ethereal_chains'])
            if attack == 'void_slash':
                dmg = random.randint(40, 60)
                game_state['hp'] -= dmg
                print(f"Cifer performs Void Slash, a blade of pure nothingness, dealing {dmg} damage!")
            elif attack == 'spirit_lance':
                dmg = random.randint(35, 55)
                game_state['focus'] = max(0, game_state['focus'] - 20)
                game_state['hp'] -= dmg
                print(f"Cifer throws a Spirit Lance, dealing {dmg} damage and draining 20 of your Focus!")
            elif attack == 'hollow_gaze':
                print("Cifer's Hollow Gaze fixes upon you, making you vulnerable. You will take more damage!")
                game_state['enemy_damage_multiplier'] = 1.3 # Player will take 30% more damage
            elif attack == 'ethereal_chains':
                dmg = random.randint(25, 40)
                game_state['hp'] -= dmg
                print(f"Ethereal Chains lash out, dealing {dmg} damage and stunning you!")
                # This would require a 'player_stunned' flag to skip next turn
        
        elif phase == 2:
            attack = random.choice(['abyssal_vortex', 'soul_eruption', 'shattering_reality', 'finality'])
            if attack == 'abyssal_vortex':
                dmg = random.randint(60, 80)
                game_state['hp'] -= dmg
                print(f"Dark Rising creates an Abyssal Vortex, pulling you in for {dmg} damage!")
            elif attack == 'soul_eruption':
                dmg_over_time = random.randint(20, 30)
                print(f"Dark Rising's Soul Eruption inflicts a curse! You will take {dmg_over_time} damage for the next 2 turns.")
                # This would require a DoT effect tracker
            elif attack == 'shattering_reality':
                dmg = random.randint(50, 70)
                game_state['hp'] -= dmg
                print(f"Space cracks around you as Dark Rising Shatters Reality, dealing {dmg} damage and weakening your attacks!")
            elif attack == 'finality':
                dmg = random.randint(100, 150)
                print(f"Dark Rising charges its ultimate attack, Finality! It unleashes a massive beam of energy for {dmg} damage!")
                game_state['hp'] -= dmg
        
        sleep(2)
        if game_state.get('enemy_damage_multiplier', 1.0) != 1.0:
            print("The vulnerability from Hollow Gaze wears off.")
            game_state['enemy_damage_multiplier'] = 1.0

    if game_state['hp'] > 0:
        print("\n<< IMPOSSIBLE... >> The voice fades as the dark form dissolves into nothingness.")
        sleep(3)
        game_state['cifer_defeated'] = True
        award_exp(ALL_ENEMY_STATS['cifer']['exp_reward'])
        print("\nYou have conquered the vessel. A strange sense of peace washes over you, but you feel a pull, a transportation to somewhere new...")
        sleep(4)
        game_state['current_location'] = 'kamurocho'
        save_game()
    else:
        print("\nYou have been overwhelmed. The world fades to black.")
        # Handle player loss
        game_state['hp'] = game_state['player_max_hp'] # Revive player


def kamurocho_hub():
    global game_state
    game_state['current_location'] = 'kamurocho'
    print("\n\nYou awaken not in the fiery pits or abyssal depths, but on a rain-slicked street under a canopy of vibrant neon lights. The air smells of street food and electricity. You are in Kamurocho.")
    sleep(4)

    while True:
        print("\n--- Kamurocho Center Street ---")
        prompt = """What will you do?
1. Explore the city streets.
2. Visit the local Arcade for some minigames.
3. Find a street fighting tournament.
4. Go to a hostess club.
5. Eat at a local ramen shop (Heal).
6. Investigate the local Yakuza presence (Story).
7. Manage your Diary.
8. Save and Quit.
Choice: """
        choice = get_player_input(prompt, list(range(1, 9)))
        print()

        if choice == 1:
            print("You wander through the bustling, colorful streets of Kamurocho. It's a city that never sleeps, a maze of entertainment and danger.")
        elif choice == 2:
            print("You enter a loud, bright arcade. You could lose hours and a lot of yen here. (Minigame placeholder)")
        elif choice == 3:
            print("You find an illegal fighting ring in a back alley. Time to test your might.")
            battle_sequence('yakuza_enforcer')
        elif choice == 4:
            print("You visit a flashy hostess club. It's an interesting cultural experience, but expensive.")
        elif choice == 5:
            heal_amt = int(game_state['player_max_hp'] * 0.5)
            game_state['hp'] = min(game_state['player_max_hp'], game_state['hp'] + heal_amt)
            print(f"The ramen is delicious and revitalizing! You heal for {heal_amt} HP.")
        elif choice == 6:
            if game_state['player_clan']:
                print(f"You are a member of the {game_state['player_clan'].title()} Clan. You should head to the main office.")
                # This would lead to the next story beat after choosing a clan
            else:
                choose_clan()
            if game_state['mistral_defeated']:
                 game_state['current_location'] = 'northern_kamurocho'
                 return
        elif choice == 7:
            manage_diary()
        elif choice == 8:
            save_game()
            game_state['current_location'] = 'quit'
            return

def choose_clan():
    global game_state
    print("Your investigation leads you to the realization that to survive and get information in this city, you need protection. You need a clan.")
    sleep(3)
    print("You have three options:")
    choice = get_player_input("""
1. The Dojima Clan: Known for their sheer ferocity and power. (Buff: 'Mark of the Dragon' - 15% chance on any hit to deal 50% bonus damage.)
2. The Tojo Clan: The largest and most organized, honorable yet ruthless. (Buff: 'Mark of the Patriarch' - Start every battle with 25 ultimate charge.)
3. The Ginryu Clan: A smaller, more mysterious group known for their cunning. (Buff: 'Mark of the Silver Dragon' - All Focus gains are increased by 25%.)
Choose your allegiance: """, [1, 2, 3])

    if choice == 1:
        game_state['player_clan'] = 'dojima'
        print("You have sworn loyalty to the Dojima Clan. May your fists be like dragons.")
    elif choice == 2:
        game_state['player_clan'] = 'tojo'
        print("You have joined the prestigious Tojo Clan. Uphold its honor.")
    elif choice == 3:
        game_state['player_clan'] = 'ginryu'
        print("You are now a member of the Ginryu Clan. Outthink your enemies.")
    
    save_game()
    sleep(3)
    assassination_cutscene()

def assassination_cutscene():
    clan_leader = f"The Patriarch of the {game_state['player_clan'].title()} Clan"
    print(f"\nAs a new member, you are granted an audience with {clan_leader}. You enter his ornate office, ready to explain your plight with the Regents.")
    sleep(4)
    print(f"{clan_leader}: 'So, you're the outsider causing a stir. You have guts. Speak. Why should we care about these 'Regents' of yours?'")
    sleep(4)
    print("Before you can answer, the shoji screen door behind the Patriarch slides open silently. A woman in a sleek black suit stands there, holding two ornate pistols.")
    sleep(4)
    print("WOMAN: 'Because they pay well.'")
    sleep(2)
    print("*BANG* *BANG*")
    sleep(2)
    print(f"{clan_leader} slumps over his desk, his life extinguished in an instant. The woman, Mistral, turns her cold eyes to you.")
    sleep(3)
    print("MISTRAL: 'You're the target. He was just in the way. Let's make this quick.'")
    sleep(2)
    mistral_boss_fight()
    
def mistral_boss_fight():
    print("\n--- This will be the boss fight with Mistral! ---")
    sleep(2)
    # Full boss fight logic would go here
    game_state['mistral_defeated'] = True
    print("You have defeated Mistral.")
    mistral_self_destruct_minigame()

def mistral_self_destruct_minigame():
    print("\nWith a final gasp, Mistral activates a device on her wrist. 'If I'm going down... you're coming with me!'")
    print("A countdown appears: 30 SECONDS.")
    sleep(3)
    start_time = time()
    
    # Challenge 1
    print("A lock on the door requires a quick sequence! Type: 'DISARM'")
    answer1 = input("> ")
    if time() - start_time > 30 or answer1.strip().upper() != 'DISARM':
        print("Too slow! The explosion engulfs you!")
        game_state['hp'] = 1 # Survive with 1 HP
        game_state['current_location'] = 'northern_kamurocho'
        return
    
    print("Correct! The lock clicks open!")
    
    # Challenge 2
    print("A pressure plate puzzle! Which concept opposes 'Soleil' (Sun)? Type: 'LUNE'")
    answer2 = input("> ")
    if time() - start_time > 30 or answer2.strip().upper() != 'LUNE':
        print("Wrong answer! The explosion rips through the room!")
        game_state['hp'] = 1
        game_state['current_location'] = 'northern_kamurocho'
        return

    print("Correct! You leap off the plate as it retracts!")

    # Challenge 3
    print("Final barrier! What clan did you join? Type: 'DOJIMA', 'TOJO', or 'GINRYU'")
    answer3 = input("> ")
    if time() - start_time > 30 or answer3.strip().upper() != game_state['player_clan'].upper():
        print("Hesitation is fatal! The blast catches you!")
        game_state['hp'] = 1
        game_state['current_location'] = 'northern_kamurocho'
        return
        
    print("You shout your allegiance and the barrier recognizes your mark, shattering! You dive through the opening just as the office is obliterated behind you!")
    sleep(3)
    print("You survived.")
    game_state['current_location'] = 'northern_kamurocho'
    save_game()
    
def northern_kamurocho_hub():
    global game_state
    game_state['current_location'] = 'northern_kamurocho'
    print("\nYou catch your breath in an alleyway, the sound of the explosion still ringing in your ears. You've made your way to the northern part of the city.")
    sleep(4)

    while True:
        print("\n--- Northern Kamurocho ---")
        prompt = """What's your next move?
1. Find a place to lie low.
2. Visit the 'Dragon & Tiger' weapon shop.
3. Challenge a masterless Ronin.
4. Spend time with your gauntlets (Story).
5. Report the assassination to the clan (Story).
6. Play Mahjong.
7. Go to the batting cages.
8. Save and Quit.
Choice: """
        choice = get_player_input(prompt, list(range(1, 9)))
        print()

        if choice == 1:
            print("You find an abandoned apartment to use as a temporary hideout.")
        elif choice == 2:
            print("This shop sells both powerful weapons and healing items. A useful place.")
        elif choice == 3:
            battle_sequence('ronin')
        elif choice == 4:
            if game_state.get('gauntlet_favor'):
                print("You've already settled the argument between them.")
            else:
                gauntlet_choice()
        elif choice == 5:
            if game_state.get('has_prism_armor'):
                print("You have already informed the clan.")
            else:
                get_prism_armor()
            # After getting the armor, the story progresses
            game_state['current_location'] = 'ibis'
            return
        elif choice == 6:
            print("You try your hand at Mahjong. It's... complicated. (Minigame placeholder)")
        elif choice == 7:
            print("You vent some frustration at the batting cages.")
        elif choice == 8:
            save_game()
            game_state['current_location'] = 'quit'
            return

def gauntlet_choice():
    global game_state
    print("\nIn the quiet of your hideout, the gauntlets begin to glow, and the voices of Soleil and Lune echo in your mind, bickering.")
    sleep(3)
    print("SOLEIL: 'My way is superior! Direct, overwhelming force always wins!'")
    sleep(3)
    print("LUNE: 'Foolishness! A patient, unbreakable defense will outlast any brute! Control is true power!'")
    sleep(3)
    print("They turn to you. 'We cannot agree. Tell us, who is right? Whose philosophy is better?'")
    
    choice = get_player_input("1. Soleil's path of aggression.\n2. Lune's path of patience.\nChoose: ", [1, 2])
    
    if choice == 1:
        game_state['gauntlet_favor'] = 'soleil'
        print("\nYou agree with Soleil. 'The best defense is a good offense.'")
        sleep(2)
        print("SOLEIL: 'Ha! See? True strength recognizes itself!' (You feel a permanent surge of power. Your attacks will now deal slightly more damage.)")
    else:
        game_state['gauntlet_favor'] = 'lune'
        print("\nYou agree with Lune. 'To endure is to win.'")
        sleep(2)
        print("LUNE: 'Wisdom. A shield is more reliable than a sword.' (You feel a permanent sense of resilience. You will now take slightly less damage from all attacks.)")

    save_game()

def get_prism_armor():
    global game_state
    print("\nYou cautiously return to your clan's headquarters. The members are in mourning, but they see you and their expressions turn to respect.")
    sleep(4)
    print(f"ACTING PATRIARCH: 'You... you avenged the Patriarch. You survived an attack from one of the Regent's elites. The {game_state['player_clan'].title()} Clan is in your debt.'")
    sleep(4)
    print("'Take this. It is our clan's greatest treasure. May it protect you from the dangers ahead.'")
    sleep(3)
    print("\n--- You have received the Prism Armor! ---")
    game_state['has_prism_armor'] = True
    
    # Apply stat boosts
    game_state['player_max_hp'] += 25
    game_state['hp'] = game_state['player_max_hp']
    game_state['player_base_dmg_min'] += 5
    game_state['player_base_dmg_max'] += 5
    game_state['max_focus'] += 15
    game_state['focus'] = game_state['max_focus']
    
    print("All of your stats have been enhanced!")
    print(f"Max HP: {game_state['player_max_hp']}, Base Damage: {game_state['player_base_dmg_min']}-{game_state['player_base_dmg_max']}, Max Focus: {game_state['max_focus']}")
    print("The armor also provides a passive damage reduction.")
    sleep(3)
    print("\nWith your new armor and the clan's blessing, you know you can't stay in Kamurocho. The Regents will send more. You need to find new allies, a new front for this war.")
    save_game()
    
def main():
    global game_state
    print("--- WELCOME TO NEIL'S RPG ---")
    
    while True:
        menu_choice = get_player_input("""
1. New Game
2. Load Game
3. Quit
Choice: """, [1, 2, 3])
        if menu_choice == 1:
            while True:
                username = input("Please enter your hero's name: ").strip()
                if username:
                    break
                print("Username cannot be empty.")
            start_new_game(username)
            break
        elif menu_choice == 2:
            username = input("Enter the name of the hero you want to load: ").strip()
            if load_game(username):
                print(f"\nWelcome back, {game_state['username']}! Resuming your adventure at {game_state['current_location'].replace('_', ' ').title()}.")
                sleep(2)
                break
            else:
                continue
        elif menu_choice == 3:
            print("Farewell, adventurer.")
            return
            
    while game_state['current_location'] != 'quit':
        location = game_state.get('current_location', 'act_1_intro')
        if location == 'act_1_intro': act_1_intro_hub()
        elif location == 'silverville': silverville_hub()
        elif location == 'mansion_of_heroes': mansion_of_heroes_hub()
        elif location == 'creepwood': creepwood_hub()
        elif location == 'mole_city': mole_city_and_brig_base_hub()
        elif location == 'regents_confrontation': regents_confrontation()
        elif location == 'trimbolton': trimbolton_hub()
        elif location == 'sea_voyage': start_sea_voyage()
        elif location == 'ebott_bay': act_4_ebott_bay()
        elif location == 'post_leat_camp': post_leat_camp_hub()
        elif location == 'ebott_town_hub': ebott_town_hub()
        elif location == 'abandoned_outpost': abandoned_outpost_hub()
        elif location == 'gardina': gardina_hub()
        elif location == 'act_4_opening': act_4_opening_cutscene()
        elif location == 'fork_in_the_road': fork_in_the_road_hub()
        elif location == 'fernit_path': fernit_path_hub()
        elif location == 'taph_path': taph_path_hub()
        elif location == 'kamurocho': kamurocho_hub()
        elif location == 'northern_kamurocho': northern_kamurocho_hub()
        else:
            print(f"Error: Unknown location '{location}'. Returning to start.")
            game_state['current_location'] = 'act_1_intro'
            
    print("\nThank you for playing Neil's RPG!")

def start_new_game(username):
    global game_state
    game_state = get_new_game_state()
    game_state['username'] = username
    game_state['current_location'] = 'act_1_intro'
    print(f"A new adventure begins for {username}!")
    sleep(1)

if __name__ == "__main__":
    main()