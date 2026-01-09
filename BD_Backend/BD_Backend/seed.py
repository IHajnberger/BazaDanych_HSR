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
        # The DPS Characters
        # ------------------------------------

        # ---- do uzupe³nienia ----

        # ------------------------------------
        # The Support Characters
        # ------------------------------------

        # Bronya
        skill1_bronya = Skill(Name="Combat Redeployment", Description="Boosts ally ATK and advances their action.", CharacterName="Bronya")
        skill2_bronya = Skill(Name="The Belobog March", Description="Provides team-wide damage buff.", CharacterName="Bronya")
        db.session.add_all([skill1_bronya, skill2_bronya])
        # Sunday
        skill1_sunday = Skill(Name="Benison of Paper and Rites", Description="Boosts ally DMG, CritRate and advances their action.", CharacterName="Sunday")
        skill2_sunday = Skill(Name="Ode to Caress and Cicatrix", Description="Regenerates ally energy and increases CritDMG", CharacterName="Sunday")
        db.session.add_all([skill1_sunday, skill2_sunday])
        #RuanMei
        skill1_ruanmei = Skill(Name="String Sings Slow Swirls", Description="Ruan Mei gains Overtone, giving all allies DMG and Weakness Break Efficiency boost.", CharacterName="Ruan Mei")
        skill2_ruanmei = Skill(Name="Inert Respiration", Description="Increases Break Effect and SPD for allies", CharacterName="Ruan Mei")
        db.session.add_all([skill1_ruanmei, skill2_ruanmei])
        #Sparkle
        skill1_sparkle = Skill(Name="Dreamdiver", Description="Increases allies' CritDMG and ATK, and at the same time Advances Forward ally's action", CharacterName="Sparkle")
        skill2_sparkle = Skill(Name="The Hero with a Thousand Faces", Description="Recovers 4 Skill Points for the team and grants all allies DMG boost", CharacterName="Sparkle")
        db.session.add_all([skill1_sparkle, skill2_sparkle])
        #Robin
        skill1_robin = Skill(Name="Pinion's Aria", Description="Boosts ally DMG and CritDMG", CharacterName="Robin")
        skill2_robin =  Skill(Name="Vox Harmonique, Opus Cosmique", Description="Robin enters the Concerto state and gives her allies buffs.", CharacterName="Robin")
        db.session.add_all([skill1_robin, skill2_robin])
        #Tribbie
        skill1_tribbie = Skill(Name="Where'd the Gifts Go", Description="Gains Numinosity, increases all ally targets' All-Type RES PEN", CharacterName="Tribbie")
        skill2_tribbie = Skill(Name="Guess Who Lives Here", Description="Activates a Zone and deals Quantum DMG, additionaly increases enemy targets' DMG taken", CharacterName="Tribbie")
        db.session.add_all([skill1_tribbie, skill2_tribbie])
        #Cerydra
        skill1_cerydra = Skill(Name="Pawn's Promotion", Description="Grants Military Merit to one designated ally, buffing the character", CharacterName="Cerydra")
        skill2_cerydra = Skill(Name="Scholar's Mate", Description="Gains 2 Charge of Military Merit or grants it anew", CharacterName="Cerydra")
        db.session.add_all([skill1_cerydra, skill2_cerydra])
        #Jiaoqiu
        skill1_jiaoqiu= Skill(Name="Scorch Onslaught", Description="Deals Fire DMG and inflicts 1 stack of Ashen Roast on the primary target", CharacterName="Jiaoqiu")
        skill2_jiaoqiu = Skill(Name="Pyrograph Arcanum", Description="Sets the number of Ashen Roast on max, while in zone enemy targets receive higher DMG", CharacterName="Jiaoqiu")
        db.session.add_all([skill1_jiaoqiu, skill2_jiaoqiu])
        #Fugue
        skill1_fugue = Skill(Name="Virtue Beckons Bliss", Description="Grants one designated ally Foxian Prayer, increasing their Break Effect", CharacterName="Fugue")
        skill2_fugue = Skill(Name="Solar Splendor Shines Upon All", Description="Deals Fire DMG to all enemies", CharacterName="Fugue")
        db.session.add_all([skill1_fugue, skill2_fugue])
        #TheDahlia
        skill1_thedahlia = Skill(Name="Lick... Enkindled Betrayal", Description="Deploys a Zone, while it lasts increases all allies' Weakness Break Efficiency", CharacterName="The Dahlia")
        skill2_thedahlia = Skill(Name="Wallow... Entombed Ash", Description="Inflicts a Wilt state on all enemies, reducing their def and implanting Weakness ", CharacterName="The Dahlia")
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
        skill2_ruanmei.Effects.extend([eff_breakeff_50, eff_spd_8])
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
        
        #Gepard
        skill_gepard.Effects.extend([eff_critdmg_15])
        #FuXuan
        skill_fuxuan.Effects.extend([eff_critrate_12, eff_hp_6, eff_critdmg_10])
        #Aventurine
        skill_aventurine.Effects.extend([eff_critdmg_40])
        #PermansorTerrae
        skill_pt.Effects.extend([eff_atk_35, eff_critdmg_10])
        
        #Hyacine
        skill_hyacine.Effects.extend([eff_hp_34])
        #Bailu
        skill_bailu.Effects.extend([eff_critdmg_15])
        #Huohuo
        skill_huohuo.Effects.extend([eff_atk_24, eff_critdmg_15, eff_energy_15])
        #Luocha
        skill_luocha.Effects.extend([eff_critdmg_15])
        #Lingsha
        skill_lingsha.Effects.extend([eff_breakeff_20])
        
        # ====================================
        # 6. Commit wszystkich zmian
        # ====================================
        db.session.commit()
        #print("CHAR AFTER:", Character.query.count())  # test po seedzie
        #print("SEED COMPLETE")

if __name__ == "__main__":
    run_seed()
