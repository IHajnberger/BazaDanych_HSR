from __init__ import create_app
from extensions import db

from models.Character import Character
from models.Skill import Skill
from models.Effect import Effect
from models.Need import Need

def run_seed():
    app = create_app()
    with app.app_context():

        # print("CHAR BEFORE:", Character.query.count())  # test przed seedem

        # ====================================
        # 1. REQUIREMENTS (Need)
        # ====================================
        need_atk = Need(Require="ATK")
        need_critDMG = Need(Require="CRITDMG")
        need_critRATE = Need(Require="CRITRATE")
        need_spd = Need(Require="SPD")
        need_hp = Need(Require="HP")
        need_DMG = Need(Require="DMG")
        need_breakEffect = Need(Require="BREAKEFFECT")
        need_energy = Need(Require="ENERGY")
        need_atp = Need(Require="ATP") #All-Type RES PEN
        db.session.add_all([need_atp, need_atk, need_critDMG, need_critRATE, need_spd, need_hp, need_DMG, need_breakEffect, need_energy])

        # ====================================
        # 2. CHARACTERS
        # ====================================

        # ------------------------------------
        # The DPS Characters
        # ------------------------------------
        
        # The Hunt
        Seele = Character(Name="Seele", Role="DPS", Element="Quantum", Path="Hunt")
        db.session.add(Seele)
        Seele.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd, need_DMG, need_atp])

        Yanqing = Character(Name="Yanqing", Role="DPS", Element="Ice", Path="Hunt")
        db.session.add(Yanqing)
        Yanqing.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd, need_DMG, need_atp])

        Feixiao = Character(Name="Feixiao", Role="DPS", Element="Wind", Path="Hunt")
        db.session.add(Feixiao)
        Feixiao.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd, need_DMG, need_atp])

        Boothill = Character(Name="Boothill", Role="DPS", Element="Physical", Path="Hunt")
        db.session.add(Boothill)
        Boothill.Needs.extend([need_breakEffect, need_critDMG, need_critRATE, need_spd, need_DMG, need_atp])

        Topaz = Character(Name="Topaz", Role="DPS", Element="Fire", Path="Hunt")
        db.session.add(Topaz)
        Topaz.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd, need_DMG, need_atp])

        DrRatio = Character(Name="Dr.Ratio", Role="DPS", Element="Imaginary", Path="Hunt")
        db.session.add(DrRatio)
        DrRatio.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd, need_DMG, need_atp])

        # The Destruction
        Blade = Character(Name="Blade", Role="DPS", Element="Wind", Path="Destruction")
        db.session.add(Blade)
        Blade.Needs.extend([need_hp, need_critDMG, need_critRATE, need_spd, need_DMG, need_atp])

        Clara = Character(Name="Clara", Role="DPS", Element="Physical", Path="Destruction")
        db.session.add(Clara)
        Clara.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_atp])

        ImbibitorLunae = Character(Name="Imbibitor Lunae", Role="DPS", Element="Imaginary", Path="Destruction")
        db.session.add(ImbibitorLunae)
        ImbibitorLunae.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        Jingliu = Character(Name="Jingliu", Role="DPS", Element="Ice", Path="Destruction")
        db.session.add(Jingliu)
        Jingliu.Needs.extend([need_hp, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        Firefly = Character(Name="Firefly", Role="DPS", Element="Fire", Path="Destruction")
        db.session.add(Firefly)
        Firefly.Needs.extend([need_atk, need_breakEffect, need_DMG, need_spd, need_atp])

        Yunli = Character(Name="Yunli", Role="DPS", Element="Physical", Path="Destruction")
        db.session.add(Yunli)
        Yunli.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_atp])

        Mydei = Character(Name="Mydei", Role="DPS", Element="Imaginary", Path="Destruction")
        db.session.add(Mydei)
        Mydei.Needs.extend([need_hp, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        Phainon = Character(Name="Phainon", Role="DPS", Element="Physical", Path="Destruction")
        db.session.add(Phainon)
        Phainon.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        # The Erudition
        Argenti = Character(Name="Argenti", Role="DPS", Element="Physical", Path="Erudition")
        db.session.add(Argenti)
        Argenti.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        Himeko = Character(Name="Himeko", Role="DPS", Element="Fire", Path="Erudition")
        db.session.add(Himeko)
        Himeko.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        JingYuan = Character(Name="Jing Yuan", Role="DPS", Element="Lightning", Path="Erudition")
        db.session.add(JingYuan)
        JingYuan.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        Jade = Character(Name="Jade", Role="DPS", Element="Quantum", Path="Erudition")
        db.session.add(Jade)
        Jade.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        Rappa = Character(Name="Rappa", Role="DPS", Element="Imaginary", Path="Erudition")
        db.session.add(Rappa)
        Rappa.Needs.extend([need_atk, need_breakEffect, need_DMG, need_spd, need_atp])

        TheHerta = Character(Name="The Herta", Role="DPS", Element="Ice", Path="Erudition")
        db.session.add(TheHerta)
        TheHerta.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        Anaxa = Character(Name="Anaxa", Role="DPS", Element="Wind", Path="Erudition")
        db.session.add(Anaxa)
        Anaxa.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        # The Remembrance
        Aglaea = Character(Name="Aglaea", Role="DPS", Element="Lightning", Path="Remembrance")
        db.session.add(Aglaea)
        Aglaea.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd, need_energy, need_atp])

        Castorice = Character(Name="Castorice", Role="DPS", Element="Quantum", Path="Remembrance")
        db.session.add(Castorice)
        Castorice.Needs.extend([need_hp, need_critDMG, need_critRATE, need_DMG, need_atp])

        Evernight = Character(Name="Evernight", Role="DPS", Element="Ice", Path="Remembrance")
        db.session.add(Evernight)
        Evernight.Needs.extend([need_hp, need_critDMG, need_critRATE, need_DMG, need_spd, need_atp])

        # The Nihility
        Kafka = Character(Name="Kafka", Role="DPS", Element="Lightning", Path="Nihility")
        db.session.add(Kafka)
        Kafka.Needs.extend([need_atk, need_DMG, need_spd, need_atp])

        Welt = Character(Name="Welt", Role="DPS", Element="Imaginary", Path="Nihility")
        db.session.add(Welt)
        Welt.Needs.extend([need_atk, need_DMG, need_spd, need_critDMG, need_critRATE, need_atp])

        BlackSwan = Character(Name="Black Swan", Role="DPS", Element="Wind", Path="Nihility")
        db.session.add(BlackSwan)
        BlackSwan.Needs.extend([need_atk, need_DMG, need_spd, need_atp])

        Acheron = Character(Name="Acheron", Role="DPS", Element="Lightning", Path="Nihility")
        db.session.add(Acheron)
        Acheron.Needs.extend([need_atk, need_DMG, need_spd, need_critDMG, need_critRATE, need_atp])

        Cipher = Character(Name="Cipher", Role="DPS", Element="Quantum", Path="Nihility")
        db.session.add(Cipher)
        Cipher.Needs.extend([need_atk, need_DMG, need_spd, need_critDMG, need_critRATE, need_atp])

        Hysilens = Character(Name="Hysilens", Role="DPS", Element="Physical", Path="Nihility")
        db.session.add(Hysilens)
        Hysilens.Needs.extend([need_atk, need_DMG, need_spd, need_atp])

        # ------------------------------------
        # The Support Characters
        # ------------------------------------

        # The Harmony 
        Bronya = Character(Name="Bronya", Role="Support", Element="Wind", Path="Harmony")
        db.session.add(Bronya)

        Sunday = Character(Name="Sunday", Role="Support", Element="Imaginary", Path="Harmony")
        db.session.add(Sunday)

        RuanMei = Character(Name="Ruan Mei", Role="Support", Element="Ice", Path="Harmony")
        db.session.add(RuanMei)
        
        Sparkle = Character(Name="Sparkle", Role="Support", Element="Quantum", Path="Harmony")
        db.session.add(Sparkle)
        
        Robin = Character(Name="Robin", Role="Support", Element="Physical", Path="Harmony")
        db.session.add(Robin)
        
        Tribbie = Character(Name="Tribbie", Role="Support", Element="Quantum", Path="Harmony")
        db.session.add(Tribbie)
        
        Cerydra = Character(Name="Cerydra", Role="Support", Element="Wind", Path="Harmony")
        db.session.add(Cerydra)

        # The Nihility
        Jiaoqiu = Character(Name="Jiaoqiu", Role="Support", Element="Fire", Path="Nihility")
        db.session.add(Jiaoqiu)

        Fugue = Character(Name="Fugue", Role="Support", Element="Fire", Path="Nihility")
        db.session.add(Fugue)

        TheDahlia = Character(Name="The Dahlia", Role="Support", Element="Fire", Path="Nihility")
        db.session.add(TheDahlia)

        # ------------------------------------
        # The Sustain Characters
        # ------------------------------------

        # The Preservation

        Gepard = Character(Name="Gepard", Role="Sustain", Element="Ice", Path="Preservation")
        db.session.add(Gepard)

        FuXuan = Character(Name="Fu Xuan", Role="Sustain", Element="Quantum", Path="Preservation")
        db.session.add(FuXuan)

        Aventurine = Character(Name="Aventurine", Role="Sustain", Element="Imaginary", Path="Preservation")
        db.session.add(Aventurine)

        PermansorTerrae = Character(Name="Permansor Terrae", Role="Sustain", Element="Physical", Path="Preservation")
        db.session.add(PermansorTerrae)
        
        # The Remembrance

        Hyacine = Character(Name="Hyacine", Role="Sustain", Element="Wind", Path="Remembrance")
        db.session.add(Hyacine)

        # The Abudance 
        
        Bailu = Character(Name="Bailu", Role="Sustain", Element="Lightning", Path="Abundance")
        db.session.add(Bailu)

        Luocha = Character(Name="Luocha", Role="Sustain", Element="Imaginary", Path="Abundance")
        db.session.add(Luocha)

        Huohuo = Character(Name="Huohuo", Role="Sustain", Element="Wind", Path="Abundance")
        db.session.add(Huohuo)

        Lingsha = Character(Name="Lingsha", Role="Sustain", Element="Fire", Path="Abundance")
        db.session.add(Lingsha)

        # ====================================
        # 3. SKILLS
        # ====================================
        
        # ------------------------------------
        # The DPS Characters - place holders
        # ------------------------------------

        # Seele-Fixed
        skill1_seele= Skill(Name="Sheathed Blade", Description="Deals Quantum DMG to a single enemy. Seele gains big SPD buff for 2 turn(s).", CharacterName="Seele")
        skill2_seele= Skill(Name="Butterfly Flurry", Description="Seele enters the buffed state and deals Quantum DMG to a single enemy.", CharacterName="Seele")
        db.session.add_all([skill1_seele, skill2_seele])

        # Yanqing-Fixed
        skill1_yanqing= Skill(Name="Darting Ironthorn", Description="Deals Ice DMG to a single enemy and activates Soulsteel Sync Link for 1 turn.", CharacterName="Yanqing")
        skill2_yanqing= Skill(Name="Amidst the Raining Bliss", Description="Increases Yanqing's crit RATE. When Soulsteel Sync is active, increases Yanqing's crit DMG. Afterwards, deals Ice DMG to a single enemy.", CharacterName="Yanqing")
        db.session.add_all([skill1_yanqing, skill2_yanqing])

        # Feixiao-Fixed
        skill1_feixiao= Skill(Name="Waraxe", Description="Deals Wind DMG to a target enemy. Then, immediately launches 1 instance of Talent's follow-up attack against the target.", CharacterName="Feixiao")
        skill2_feixiao= Skill(Name="Terrasplit", Description="Deals increased Wind DMG to a single target enemy. During this time, can ignore Weakness Type to reduce the target's Toughness. During the attack, Feixiao first launches Boltsunder Blitz or Waraxe Skyward on the target, for a total of 6 time(s).", CharacterName="Feixiao")
        db.session.add_all([skill1_feixiao, skill2_feixiao])

        # Boothill-Fixed
        skill1_boothill= Skill(Name="Sizzlin' Tango", Description="Forces Boothill and a single target enemy into the Standoff state. Boothill's Basic ATK gets Enhanced, and he cannot use his Skill. After this target is defeated or becomes Weakness Broken, Boothill gains 1 stack of Pocket Trickshot. Each stack of Pocket Trickshot increases the Enhanced Basic Attack's Toughness Reduction", CharacterName="Boothill")
        skill2_boothill= Skill(Name="Dust Devil's Sunset Rodeo", Description="Applies Physical Weakness to a single target enemy. Deals Physical DMG to the target and delays their action.", CharacterName="Boothill")
        db.session.add_all([skill1_boothill, skill2_boothill])

        # Topaz-Fixed
        skill1_topaz= Skill(Name="Difficulty Paying?", Description="Inflicts a single target enemy with a Proof of Debt status, increasing the DMG it takes from follow-up attacks. If there are no enemies inflicted with Proof of Debt on the field when an ally's turn starts or when an ally takes action, Topaz will inflict a random enemy with Proof of Debt", CharacterName="Topaz")
        skill2_topaz= Skill(Name="Turn a Profit!", Description=" Numby enters the Windfall Bonanza! state and its DMG multiplier and crit DMG increases. Also, when enemies with Proof of Debt are hit by an ally's Basic ATK, Skill, or Ultimate, Numby's action is Advanced Forward.", CharacterName="Topaz")
        db.session.add_all([skill1_topaz, skill2_topaz])

        # Dr.Ratio-Fixed
        skill1_drratio= Skill(Name="Intellectual Midwifery", Description="Deals part of Dr. Ratio's ATK as Imaginary DMG to a single target enemy.", CharacterName="Dr.Ratio")
        skill2_drratio= Skill(Name="Syllogistic Paradox", Description="Deals Imaginary DMG to a single target enemy and applies Wiseman's Folly. When Dr. Ratio's allies attack a target afflicted with Wiseman's Folly, Dr. Ratio launches his Talent's follow-up attack.", CharacterName="Dr.Ratio")
        db.session.add_all([skill1_drratio, skill2_drratio])

        # Blade-Fixed
        skill1_blade= Skill(Name="Hellscape", Description="Consumes part HP of Blade's Max HP to enter the Hellscape state. While under this state, his Skill cannot be used, his DMG dealt and the chance of receiving attacks from enemy targets increase.His Basic ATK Shard Sword is enhanced to Forest of Swords.", CharacterName="Blade")
        skill2_blade= Skill(Name="Death Sentence", Description="Sets Blade's current HP to 50% of his Max HP and deals Wind DMG to one designated enemy and the tally of Blade's HP loss in the current battle. At the same time, deals Wind DMG to adjacent targets.", CharacterName="Blade")
        db.session.add_all([skill1_blade, skill2_blade])

        # Clara-Fixed
        skill1_clara= Skill(Name="Svarog Watches Over You", Description="Deals Physical DMG to all enemies, and additionally deals Physical DMG equal to part of Clara's ATK to enemies marked by Svarog with a Mark of Counter.", CharacterName="Clara")
        skill2_clara= Skill(Name="Promise, Not Command", Description="After Clara uses Ultimate, DMG dealt to her is reduced, and she has greatly increased chance of being attacked by enemies for 2 turn(s). In addition, Svarog's Counter is enhanced, when an ally is attacked, Svarog immediately launches a Counter, and its DMG multiplier on the enemy increases.", CharacterName="Clara")
        db.session.add_all([skill1_clara, skill2_clara])

        # Imbibitor Lunae-Fixed
        skill1_imbibitorlunae= Skill(Name="Dracore Libre", Description=" Enhances Basic ATK using skill points. Enhancements may be applied up to 3 times consecutively.", CharacterName="Imbibitor Lunae")
        skill2_imbibitorlunae= Skill(Name="Azure Aqua's Ablutes All", Description="Uses a 3-hit attack and deals Imaginary DMG to a single target. At the same time, deals Imaginary DMG equal to part of Imbibitor Lunae's ATK to adjacent enemies. Then, obtains 2 Squama Sacrosancta - which can be used to offset Imbibitor Lunae's consumption of skill points.", CharacterName="Imbibitor Lunae")
        db.session.add_all([skill1_imbibitorlunae, skill2_imbibitorlunae])

        # Jingliu-Fixed
        skill1_jingliu= Skill(Name="Transcendent Flash | Moon on Glacial River", Description="Deals Ice DMG based on Jingliu's Max HP to one designated enemy and gains 1 stack(s) of Syzygy. When Jingliu has 2 stacks of Syzygy she enters the Spectral Transmigration state. Then Jingliu's Skill is enhanced to Moon On Glacial River. Enhanced skill deals Ice DMG based of Jingliu's Max HP to one designated enemy, and deals additional to adjacent enemies.", CharacterName="Jingliu")
        skill2_jingliu= Skill(Name="Florephemeral Dreamflux", Description="Deals Ice DMG to one designated enemy, and deals additional Ice DMG equal to their adjacent enemies, gains 1 stack(s) of Syzygy", CharacterName="Jingliu")
        db.session.add_all([skill1_jingliu, skill2_jingliu])

        # Firefly-Fixed
        skill1_firefly= Skill(Name="Order: Aerial Bombardment | Fyrefly Type-IV: Deathstar Overload", Description="Consumes part of SAM's Max HP and regenerates a fixed amount of Energy. Deals Fire DMG to a single target enemy. Upon entering the Complete Combustion state gains Enhanced Skill. When enhanced Restores small amount of this unit's Max HP. Applies Fire Weakness to a single target enemy, lasting for 2 turn(s). Deals enchanced Fire DMG to this target. At the same time, deals Fire DMG to adjacent targets.", CharacterName="Firefly")
        skill2_firefly= Skill(Name="Fyrefly Type-IV: Complete Combustion", Description="Firefly enters the Complete Combustion state enhancing her Basic Attack, Skill and buffing her SPD and Weakness Break efficiency.", CharacterName="Firefly")
        db.session.add_all([skill1_firefly, skill2_firefly])

        # Yunli-Fixed
        skill1_yunli= Skill(Name="Bladeborne Quake", Description="Restores small part of Yunli's HP. Deals Physical DMG to a single target enemy and smaller Physical DMG to adjacent targets.", CharacterName="Yunli")
        skill2_yunli= Skill(Name="Earthbind, Etherbreak", Description="Yunli gains Parry and Taunts all enemies, lasting until the end of the next ally's or enemy's turn also increasing her stats. When triggering the Counter effect from Talent, launches the Counter Intuit: Cull instead and removes the Parry effect. If no Counter is triggered while Parry is active, Yunli will immediately launch the Counter Intuit: Slash on a random enemy target, both dealing Physical DMG of different amount.", CharacterName="Yunli")
        db.session.add_all([skill1_yunli, skill2_yunli])

        # Mydei
        skill1_mydei= Skill(Name="Phantom Strike", Description="Deals Imaginary DMG to a single target enemy, inflicting Imaginary Charge.", CharacterName="Mydei")
        skill2_mydei= Skill(Name="Spectral Onslaught", Description="After using her Skill, Mydei gains Phantom Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="Mydei")
        db.session.add_all([skill1_mydei, skill2_mydei])

        # Phainon
        skill1_phainon= Skill(Name="Gravity Slash", Description="Deals Physical DMG to a single target enemy, ignoring their Weakness Type to reduce their Toughness.", CharacterName="Phainon")
        skill2_phainon= Skill(Name="Singularity Crash", Description="After using his Skill, Phainon gains Gravity Charge, increasing his CRIT DMG and DMG dealt.", CharacterName="Phainon")
        db.session.add_all([skill1_phainon, skill2_phainon])

        # Argenti
        skill1_argenti= Skill(Name="Tempest Blade", Description="Deals Wind DMG to a single target enemy, inflicting Wind Charge.", CharacterName="Argenti")
        skill2_argenti= Skill(Name="Hurricane Slash", Description="After using his Skill, Argenti gains Storm Charge, increasing his CRIT DMG and DMG dealt.", CharacterName="Argenti")
        db.session.add_all([skill1_argenti, skill2_argenti])

        # Himeko
        skill1_himeko= Skill(Name="Blazing Sword", Description="Deals Fire DMG to a single target enemy, inflicting Burn.", CharacterName="Himeko")
        skill2_himeko= Skill(Name="Inferno Strike", Description="After using her Skill, Himeko gains Flame Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="Himeko")
        db.session.add_all([skill1_himeko, skill2_himeko])

        # JingYuan
        skill1_jingyuan= Skill(Name="Thunderous Slash", Description="Deals Lightning DMG to a single target enemy, inflicting Shock.", CharacterName="Jing Yuan")
        skill2_jingyuan= Skill(Name="Stormbreaker", Description="After using his Skill, Jing Yuan gains Thunder Charge, increasing his CRIT DMG and DMG dealt.", CharacterName="Jing Yuan")
        db.session.add_all([skill1_jingyuan, skill2_jingyuan])

        # Jade
        skill1_jade= Skill(Name="Quantum Edge", Description="Deals Quantum DMG to a single target enemy, inflicting Quantum Charge.", CharacterName="Jade")
        skill2_jade= Skill(Name="Entropic Slash", Description="After using her Skill, Jade gains Quantum Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="Jade")
        db.session.add_all([skill1_jade, skill2_jade])

        # Rappa
        skill1_rappa= Skill(Name="Void Strike", Description="Deals Imaginary DMG to a single target enemy, inflicting Imaginary Charge.", CharacterName="Rappa")
        skill2_rappa= Skill(Name="Abyssal Onslaught", Description="After using his Skill, Rappa gains Void Charge, increasing his CRIT DMG and DMG dealt.", CharacterName="Rappa")
        db.session.add_all([skill1_rappa, skill2_rappa])
        
        # The Herta
        skill1_theherta= Skill(Name="Frost Edge", Description="Deals Ice DMG to a single target enemy, inflicting Frostbite.", CharacterName="The Herta")
        skill2_theherta= Skill(Name="Glacial Slash", Description="After using her Skill, The Herta gains Glacier Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="The Herta")
        db.session.add_all([skill1_theherta, skill2_theherta])

        # Anaxa
        skill1_anaxa= Skill(Name="Gale Blade", Description="Deals Wind DMG to a single target enemy, inflicting Wind Charge.", CharacterName="Anaxa")
        skill2_anaxa= Skill(Name="Tempest Slash", Description="After using her Skill, Anaxa gains Storm Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="Anaxa")
        db.session.add_all([skill1_anaxa, skill2_anaxa])

        # Aglaea
        skill1_aglaea= Skill(Name="Lightning Strike", Description="Deals Lightning DMG to a single target enemy, inflicting Shock.", CharacterName="Aglaea")
        skill2_aglaea= Skill(Name="Thunderclap Assault", Description="After using her Skill, Aglaea gains Thunder Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="Aglaea")
        db.session.add_all([skill1_aglaea, skill2_aglaea])

        # Castorice
        skill1_castorice= Skill(Name="Quantum Blast", Description="Deals Quantum DMG to a single target enemy, inflicting Quantum Charge.", CharacterName="Castorice")
        skill2_castorice= Skill(Name="Entropic Barrage", Description="After using her Skill, Castorice gains Quantum Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="Castorice")
        db.session.add_all([skill1_castorice, skill2_castorice])

        # Evernight
        skill1_evernight= Skill(Name="Frost Nova", Description="Deals Ice DMG to a single target enemy, inflicting Frostbite.", CharacterName="Evernight")
        skill2_evernight= Skill(Name="Glacial Storm", Description="After using her Skill, Evernight gains Glacier Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="Evernight")
        db.session.add_all([skill1_evernight, skill2_evernight])

        # Kafka
        skill1_kafka= Skill(Name="Thunder Slash", Description="Deals Lightning DMG to a single target enemy, inflicting Shock.", CharacterName="Kafka")
        skill2_kafka= Skill(Name="Storm Surge", Description="After using her Skill, Kafka gains Thunder Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="Kafka")
        db.session.add_all([skill1_kafka, skill2_kafka])

        # Welt
        skill1_welt= Skill(Name="Void Blade", Description="Deals Imaginary DMG to a single target enemy, inflicting Imaginary Charge.", CharacterName="Welt")
        skill2_welt= Skill(Name="Abyssal Slash", Description="After using his Skill, Welt gains Void Charge, increasing his CRIT DMG and DMG dealt.", CharacterName="Welt")
        db.session.add_all([skill1_welt, skill2_welt])

        # Black Swan
        skill1_blackswan= Skill(Name="Gale Strike", Description="Deals Wind DMG to a single target enemy, inflicting Wind Charge.", CharacterName="Black Swan")
        skill2_blackswan= Skill(Name="Tempest Assault", Description="After using her Skill, Black Swan gains Storm Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="Black Swan")
        db.session.add_all([skill1_blackswan, skill2_blackswan])

        # Acheron
        skill1_acheron= Skill(Name="Thunder Blade", Description="Deals Lightning DMG to a single target enemy, inflicting Shock.", CharacterName="Acheron")
        skill2_acheron= Skill(Name="Storm Slash", Description="After using his Skill, Acheron gains Thunder Charge, increasing his CRIT DMG and DMG dealt.", CharacterName="Acheron")
        db.session.add_all([skill1_acheron, skill2_acheron])

        # Cipher
        skill1_cipher= Skill(Name="Quantum Strike", Description="Deals Quantum DMG to a single target enemy, inflicting Quantum Charge.", CharacterName="Cipher")
        skill2_cipher= Skill(Name="Entropic Assault", Description="After using his Skill, Cipher gains Quantum Charge, increasing his CRIT DMG and DMG dealt.", CharacterName="Cipher")
        db.session.add_all([skill1_cipher, skill2_cipher])

        # Hysilens
        skill1_hysilens= Skill(Name="Gravity Blade", Description="Deals Physical DMG to a single target enemy, ignoring their Weakness Type to reduce their Toughness.", CharacterName="Hysilens")
        skill2_hysilens= Skill(Name="Singularity Slash", Description="After using her Skill, Hysilens gains Gravity Charge, increasing her CRIT DMG and DMG dealt.", CharacterName="Hysilens")
        db.session.add_all([skill1_hysilens, skill2_hysilens])

        # ------------------------------------
        # The Support Characters
        # ------------------------------------

        # Bronya-Fixed
        skill1_bronya = Skill(Name="Combat Redeployment", Description="Dispels a debuff from a single ally, allows them to immediately take action, and increases their DMG.", CharacterName="Bronya")
        skill2_bronya = Skill(Name="The Belobog March", Description=" Increases the ATK of all allies and increases their crit DMG.", CharacterName="Bronya")
        db.session.add_all([skill1_bronya, skill2_bronya])
        # Sunday-Fixed
        skill1_sunday = Skill(Name="Benison of Paper and Rites", Description="Enables one designated ally character and their summon to immediately take action, and increases their crit RATE and DMG dealt.", CharacterName="Sunday")
        skill2_sunday = Skill(Name="Ode to Caress and Cicatrix", Description="Regenerates energy for one designated ally character, and turns the target and their summon into The Beatified increasing their crit DMG.", CharacterName="Sunday")
        db.session.add_all([skill1_sunday, skill2_sunday])
        #RuanMei-Fixed
        skill1_ruanmei = Skill(Name="String Sings Slow Swirls", Description="After using her Skill, Ruan Mei gains Overtone, giving all allies DMG and Weakness Break Efficiency boost.", CharacterName="Ruan Mei")
        skill2_ruanmei = Skill(Name="Petals to Stream, Repose in Dream", Description="Ruan Mei deploys a field that lasts for 2 turns. While inside the field, all allies' All-Type RES PEN and Break Effect increases.", CharacterName="Ruan Mei")
        db.session.add_all([skill1_ruanmei, skill2_ruanmei])
        #Sparkle-Fixed
        skill1_sparkle = Skill(Name="Dreamdiver", Description= "Increases the CRIT DMG of a single target ally at the same time Advances Forward this ally's action.", CharacterName="Sparkle")
        skill2_sparkle = Skill(Name="The Hero with a Thousand Faces", Description="Recovers 4 Skill Points for the team and grants all allies Cipher giving them DMG boost.", CharacterName="Sparkle")
        db.session.add_all([skill1_sparkle, skill2_sparkle])
        #Robin-Fixed
        skill1_robin = Skill(Name="Pinion's Aria", Description="Increase crit DMG and DMG dealt by all allies.", CharacterName="Robin")
        skill2_robin =  Skill(Name="Vox Harmonique, Opus Cosmique", Description=" Robin enters the Concerto state and makes all other allies immediately take action. While in the Concerto state, increase all allies' ATK and crit DMG.", CharacterName="Robin")
        db.session.add_all([skill1_robin, skill2_robin])
        #Tribbie-Fixed
        skill1_tribbie = Skill(Name="Where'd the Gifts Go", Description="Gains Numinosity, increases all ally targets' All-Type RES PEN.", CharacterName="Tribbie")
        skill2_tribbie = Skill(Name="Guess Who Lives Here", Description="Activates a Zone and deals Quantum DMG, additionaly increases enemy targets' DMG taken.", CharacterName="Tribbie")
        db.session.add_all([skill1_tribbie, skill2_tribbie])
        #Cerydra-Fixed
        skill1_cerydra = Skill(Name="Pawn's Promotion", Description="Grants Military Merit to one designated ally and gives Cerydra 1 points of Charge. When Charge reaches 6 points, automatically upgrades the character to Peerage increasing their crit DMG and All-Type RES PEN. ", CharacterName="Cerydra")
        skill2_cerydra = Skill(Name="Scholar's Mate", Description="Gains 2 Charge of Military Merit. If no character on the field has it prioritizes granting it to the first character in the current team.", CharacterName="Cerydra")
        db.session.add_all([skill1_cerydra, skill2_cerydra])
        #Jiaoqiu-Fixed
        skill1_jiaoqiu= Skill(Name="Scorch Onslaught", Description="Deals Fire DMG and inflicts 1 stack of Ashen Roast on the primary target.", CharacterName="Jiaoqiu")
        skill2_jiaoqiu = Skill(Name="Pyrograph Arcanum", Description="Sets the number of Ashen Roast on max, while in zone enemy targets receive higher DMG and constant Fire DoT DMG.", CharacterName="Jiaoqiu")
        db.session.add_all([skill1_jiaoqiu, skill2_jiaoqiu])
        #Fugue-Fixed
        skill1_fugue = Skill(Name="Virtue Beckons Bliss", Description="Grants one designated ally Foxian Prayer. The ally target inflicted with it increases their Break Effect and can also reduce Toughness even when attacking enemies that don't have the corresponding Weakness Type.", CharacterName="Fugue")
        skill2_fugue = Skill(Name="Solar Splendor Shines Upon All", Description="Deals Fire DMG to all enemies ignoring their Weakness Type to reduce all enemies' Toughness.", CharacterName="Fugue")
        db.session.add_all([skill1_fugue, skill2_fugue])
        #TheDahlia-Fixed
        skill1_thedahlia = Skill(Name="Lick... Enkindled Betrayal", Description="Deploys a Zone, while it lasts increases all allies' Weakness Break Efficiency. Toughness Reduction taken by enemy targets while not Weakness Broken can also be converted into Super Break DMG.", CharacterName="The Dahlia")
        skill2_thedahlia = Skill(Name="Wallow... Entombed Ash", Description="Inflicts a Wilt state on all enemies, reducing their DEF and implanting Weakness.", CharacterName="The Dahlia")
        db.session.add_all([skill1_thedahlia, skill2_thedahlia])

        # ------------------------------------
        # The Sustain Characters
        # ------------------------------------

        #Gepard 
        skill_gepard= Skill(Name="Daunting Smite", Description="Provides shield to ally and increases target's critDMG", CharacterName="Gepard")
        db.session.add(skill_gepard)
        #FuXuan
        skill_fuxuan = Skill(Name="Known by Stars, Shown by Hearts", Description="Boosts ally max HP and increases critRate", CharacterName="Fu Xuan")
        db.session.add(skill_fuxuan)
        #Aventurine 
        skill_aventurine = Skill(Name="Roulette Shark", Description="Provides shield to ally and increases target's critDMG", CharacterName="Aventurine")
        db.session.add(skill_aventurine)
        #PermansorTerrae 
        skill_pt= Skill(Name="Terra Omnibus", Description="Provides shield to ally and increases target's ATK", CharacterName="Permansor Terrae")
        db.session.add(skill_pt)
        
        #Hyacine 
        skill_hyacine= Skill(Name="Love Over the Rainbow", Description="Summons memosprite Little Ica, restores HP for allies and increases their max HP", CharacterName="Hyacine")
        db.session.add(skill_hyacine)
        
        #Bailu
        skill_bailu= Skill(Name="Singing Among Clouds", Description="Heals 3 allies", CharacterName="Bailu")
        db.session.add(skill_bailu)
        #Luocha 
        skill_luocha= Skill(Name="Prayer of Abyss Flower", Description="After using his Skill, immediately restore the target ally's HP", CharacterName="Luocha")
        db.session.add(skill_luocha)
        #Huohuo 
        skill_huohuo= Skill(Name="Tail: Spiritual Domination:", Description="Regenerates Energy for all allies and increases their ATK", CharacterName="Huohuo")
        db.session.add(skill_huohuo)
        #Lingsha
        skill_lingsha= Skill(Name="Smoke and Splendor", Description="Deals Fire DMG to all enemies and restores HP for all allies", CharacterName="Lingsha")
        db.session.add(skill_lingsha)

        # ====================================
        # 4. EFFECTS
        # ====================================
        eff_atk_49 = Effect(Name="ATK%", Value=49)
        db.session.add(eff_atk_49)
        eff_critdmg_33 = Effect(Name="CRITDMG%", Value=33)
        db.session.add(eff_critdmg_33)
        eff_dmg_58 = Effect(Name="DMG%", Value=58)
        db.session.add(eff_dmg_58)
        eff_dmg_69 = Effect(Name="DMG%", Value=69)
        db.session.add(eff_dmg_69)
        eff_critdmg_37 = Effect(Name="CRITDMG%", Value=37)
        db.session.add(eff_critdmg_37)
        eff_critrate_18 = Effect(Name="CRITRATE%", Value=18)
        db.session.add(eff_critrate_18)
        eff_dmg_52 = Effect(Name="DMG%", Value=52)
        db.session.add(eff_dmg_52)
        eff_breakeff_50 = Effect(Name="BREAKEFFECT%", Value=50)
        db.session.add(eff_breakeff_50)
        eff_breakeff_20 = Effect(Name="BREAKEFFECT%", Value=20)
        db.session.add(eff_breakeff_20)
        eff_spd_8 = Effect(Name="SPD%", Value=8)
        db.session.add(eff_spd_8)
        eff_critdmg_69= Effect(Name="CRITDMG%", Value=69)
        db.session.add(eff_critdmg_69)
        eff_atk_15= Effect(Name="ATK%", Value=15)
        db.session.add(eff_atk_15)
        eff_dmg_28= Effect(Name="DMG%", Value=28)
        db.session.add(eff_dmg_28)
        eff_dmg_50= Effect(Name="DMG%", Value=50)
        db.session.add(eff_dmg_50)
        eff_critdmg_20= Effect(Name="CRITDMG%", Value=20)
        db.session.add(eff_critdmg_20)
        eff_atk_23= Effect(Name="ATK%", Value=23)
        db.session.add(eff_atk_23)
        eff_dmg_30= Effect(Name="DMG%", Value=30)
        db.session.add(eff_dmg_30)
        eff_critdmg_72= Effect(Name="CRITDMG%", Value=72)
        db.session.add(eff_critdmg_72)
        eff_atk_18= Effect(Name="ATK%", Value=18)
        db.session.add(eff_atk_18)
        eff_dmg_35= Effect(Name="DMG%", Value=35)
        db.session.add(eff_dmg_35)
        eff_breakeff_48= Effect(Name="BREAKEFFECT%", Value=48)
        db.session.add(eff_breakeff_48)
        eff_breakeff_30= Effect(Name="BREAKEFFECT%", Value=30)
        db.session.add(eff_breakeff_30)
        eff_breakeff_74= Effect(Name="BREAKEFFECT%", Value=74)
        db.session.add(eff_breakeff_74)
        eff_critrate_12= Effect(Name="CRITRATE%", Value=12)
        db.session.add(eff_critrate_12)
        eff_hp_6= Effect(Name="HP%", Value=6)
        db.session.add(eff_hp_6)
        eff_hp_34= Effect(Name="HP%", Value=34)
        db.session.add(eff_hp_34)
        eff_hp_20= Effect(Name="HP%", Value=20)
        db.session.add(eff_hp_20)
        eff_atk_24= Effect(Name="ATK%", Value=24)
        db.session.add(eff_atk_24)
        eff_dmg_66= Effect(Name="DMG%", Value=66)
        db.session.add(eff_dmg_66)
        eff_critdmg_28= Effect(Name="CRITDMG%", Value=28)
        db.session.add(eff_critdmg_28)
        eff_critdmg_36=Effect(Name="CRITDMG%", Value=36)
        db.session.add(eff_critdmg_36)
        eff_atk_55=Effect(Name="ATK%", Value=55)
        db.session.add(eff_atk_55)
        eff_critdmg_80=Effect(Name="CRITDMG%", Value=80)
        db.session.add(eff_critdmg_80)
        eff_dmg_80= Effect(Name="DMG%", Value=80)
        db.session.add(eff_dmg_80)
        eff_critrate_20= Effect(Name="CRITRATE%", Value=20)
        db.session.add(eff_critrate_20)
        eff_energy_20= Effect(Name="ENERGY%", Value=20)
        db.session.add(eff_energy_20)
        eff_critdmg_18= Effect(Name="CRITDMG%", Value=18)
        db.session.add(eff_critdmg_18)
        eff_dmg_18= Effect(Name="DMG%", Value=18)
        db.session.add(eff_dmg_18)
        eff_atk_120= Effect(Name="ATK%", Value=120)
        db.session.add(eff_atk_120)
        eff_atp_24= Effect(Name="ATP%", Value=24)
        db.session.add(eff_atp_24)
        eff_atk_70= Effect(Name="ATK%", Value=70)
        db.session.add(eff_atk_70)
        eff_atp_10= Effect(Name="ATP%", Value=10)
        db.session.add(eff_atp_10)
        eff_atk_60= Effect(Name="ATK%", Value=60)
        db.session.add(eff_atk_60)
        eff_spd_15= Effect(Name="SPD%", Value=15)
        db.session.add(eff_spd_15)
        eff_critdmg_10= Effect(Name="CRITDMG%", Value=10)
        db.session.add(eff_critdmg_10)
        eff_dmg_55= Effect(Name="DMG%", Value=55)
        db.session.add(eff_dmg_55)
        eff_breakeff_80= Effect(Name="BREAKEFFECT%", Value=80)
        db.session.add(eff_breakeff_80)
        eff_critdmg_15= Effect(Name="CRITDMG%", Value=15)
        db.session.add(eff_critdmg_15)
        eff_critdmg_40= Effect(Name="CRITDMG%", Value=40)
        db.session.add(eff_critdmg_40)
        eff_atk_35= Effect(Name="ATK%", Value=35)
        db.session.add(eff_atk_35)
        eff_energy_15= Effect(Name="ENERGY%", Value=15)
        db.session.add(eff_energy_15)
        eff_atp_15= Effect(Name="ATP%", Value=15)
        db.session.add(eff_atp_15)

        # ====================================
        # 5. Przypisanie efektow do skillow
        # ====================================
        #Bronya-Fixed
        skill1_bronya.Effects.extend([eff_dmg_52, eff_critdmg_28])
        skill2_bronya.Effects.extend([eff_critdmg_36, eff_atk_55])
        #Sunday-Fixed
        skill1_sunday.Effects.extend([eff_dmg_80, eff_critrate_20, eff_critdmg_28])
        skill2_sunday.Effects.extend([eff_critdmg_80,eff_energy_20])
        #RuanMei-Fixed
        skill1_ruanmei.Effects.extend([eff_dmg_52, eff_breakeff_50])
        skill2_ruanmei.Effects.extend([eff_breakeff_50, eff_spd_8, eff_atp_15])
        #Sparkle-Fixed
        skill1_sparkle.Effects.extend([eff_critdmg_80, eff_atk_15])
        skill2_sparkle.Effects.extend([eff_critdmg_28, eff_dmg_18])
        #Robin-Fixed
        skill1_robin.Effects.extend([eff_dmg_50, eff_critdmg_20])
        skill2_robin.Effects.extend([eff_atk_120])
        #Tribbie-Fixed
        skill1_tribbie.Effects.extend([eff_dmg_28, eff_atk_23, eff_atp_24])
        skill2_tribbie.Effects.extend([eff_dmg_30, eff_atk_70])
        #Cerydra-Fixed
        skill1_cerydra.Effects.extend([eff_critdmg_72, eff_atp_10 ,eff_atk_60, eff_spd_15])
        skill2_cerydra.Effects.extend([eff_critdmg_10])
        #Jiaoqiu-Fixed
        skill1_jiaoqiu.Effects.extend([eff_dmg_55])
        skill2_jiaoqiu.Effects.extend([eff_dmg_55])
        #Fuque-Fixed
        skill1_fugue.Effects.extend([eff_breakeff_80])
        skill2_fugue.Effects.extend([eff_breakeff_48])
        #TheDahlia-Fixed
        skill1_thedahlia.Effects.extend([eff_breakeff_50])
        skill2_thedahlia.Effects.extend([eff_breakeff_80])
        
        #Gepard-Fixed
        skill_gepard.Effects.extend([eff_critdmg_15])
        #FuXuan-Fixed
        skill_fuxuan.Effects.extend([eff_critrate_12, eff_hp_6, eff_critdmg_10])
        #Aventurine-Fixed
        skill_aventurine.Effects.extend([eff_critdmg_40])
        #PermansorTerrae-Fixed
        skill_pt.Effects.extend([eff_atk_35, eff_critdmg_10])
        
        #Hyacine-Fixed
        skill_hyacine.Effects.extend([eff_hp_34])
        #Bailu-Fixed
        skill_bailu.Effects.extend([eff_critdmg_15])
        #Huohuo-Fixed
        skill_huohuo.Effects.extend([eff_atk_24, eff_critdmg_15, eff_energy_15])
        #Luocha-Fixed
        skill_luocha.Effects.extend([eff_critdmg_15])
        #Lingsha-Fixed
        skill_lingsha.Effects.extend([eff_breakeff_20])
        
        # ====================================
        # 6. Commit wszystkich zmian
        # ====================================
        db.session.commit()
        #print("CHAR AFTER:", Character.query.count())  # test po seedzie
        #print("SEED COMPLETE")

if __name__ == "__main__":
    run_seed()
