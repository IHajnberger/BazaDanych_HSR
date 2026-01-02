from __init__ import create_app
from extensions import db

from models.Character import Character
from models.Skill import Skill
from models.Effect import Effect
from models.Need import Need

def run_seed():
    app = create_app()
    with app.app_context():

        print("CHAR BEFORE:", Character.query.count())  # test przed seedem

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
        need_energyRegen = Need(Require="ENERGYREGEN")
        db.session.add_all([need_atk, need_critDMG, need_critRATE, need_spd, need_hp, need_DMG, need_breakEffect, need_energyRegen])

        # ====================================
        # 2. CHARACTERS
        # ====================================

        # ------------------------------------
        # The DPS Characters
        # ------------------------------------
        
        # The Hunt
        Seele = Character(Name="Seele", Role="DPS", Element="Quantum", Path="Hunt")
        db.session.add(Seele)
        Seele.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd, need_DMG])

        Yanqing = Character(Name="Yanqing", Role="DPS", Element="Ice", Path="Hunt")
        db.session.add(Yanqing)
        Yanqing.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd, need_DMG])

        Feixiao = Character(Name="Feixiao", Role="DPS", Element="Wind", Path="Hunt")
        db.session.add(Feixiao)
        Feixiao.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd, need_DMG])

        Boothill = Character(Name="Boothill", Role="DPS", Element="Physical", Path="Hunt")
        db.session.add(Boothill)
        Boothill.Needs.extend([need_breakEffect, need_critDMG, need_critRATE, need_spd, need_DMG])

        Topaz = Character(Name="Topaz", Role="DPS", Element="Fire", Path="Hunt")
        db.session.add(Topaz)
        Topaz.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd, need_DMG])

        DrRatio = Character(Name="Dr.Ratio", Role="DPS", Element="Imaginary", Path="Hunt")
        db.session.add(DrRatio)
        DrRatio.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd, need_DMG])

        # The Destruction
        Blade = Character(Name="Blade", Role="DPS", Element="Wind", Path="Destruction")
        db.session.add(Blade)
        Blade.Needs.extend([need_hp, need_critDMG, need_critRATE, need_spd, need_DMG])

        Clara = Character(Name="Clara", Role="DPS", Element="Physical", Path="Destruction")
        db.session.add(Clara)
        Clara.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG])

        ImbibitorLunae = Character(Name="Imbibitor Lunae", Role="DPS", Element="Imaginary", Path="Destruction")
        db.session.add(ImbibitorLunae)
        ImbibitorLunae.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd])

        Jingliu = Character(Name="Jingliu", Role="DPS", Element="Ice", Path="Destruction")
        db.session.add(Jingliu)
        Jingliu.Needs.extend([need_hp, need_critDMG, need_critRATE, need_DMG, need_spd])

        Firefly = Character(Name="Firefly", Role="DPS", Element="Fire", Path="Destruction")
        db.session.add(Firefly)
        Firefly.Needs.extend([need_atk, need_breakEffect, need_DMG, need_spd])

        Yunli = Character(Name="Yunli", Role="DPS", Element="Physical", Path="Destruction")
        db.session.add(Yunli)
        Yunli.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_energyRegen])

        Mydei = Character(Name="Mydei", Role="DPS", Element="Imaginary", Path="Destruction")
        db.session.add(Mydei)
        Mydei.Needs.extend([need_hp, need_critDMG, need_critRATE, need_DMG, need_spd])

        Phainon = Character(Name="Phainon", Role="DPS", Element="Physical", Path="Destruction")
        db.session.add(Phainon)
        Phainon.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd])

        # The Erudition
        Argenti = Character(Name="Argenti", Role="DPS", Element="Physical", Path="Erudition")
        db.session.add(Argenti)
        Argenti.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd])

        Himeko = Character(Name="Himeko", Role="DPS", Element="Fire", Path="Erudition")
        db.session.add(Himeko)
        Himeko.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd])

        JingYuan = Character(Name="Jing Yuan", Role="DPS", Element="Lightning", Path="Erudition")
        db.session.add(JingYuan)
        JingYuan.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd])

        Jade = Character(Name="Jade", Role="DPS", Element="Quantum", Path="Erudition")
        db.session.add(Jade)
        Jade.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd])

        Rappa = Character(Name="Rappa", Role="DPS", Element="Imaginary", Path="Erudition")
        db.session.add(Rappa)
        Rappa.Needs.extend([need_atk, need_breakEffect, need_DMG, need_spd])

        TheHerta = Character(Name="The Herta", Role="DPS", Element="Ice", Path="Erudition")
        db.session.add(TheHerta)
        TheHerta.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd])

        Anaxa = Character(Name="Anaxa", Role="DPS", Element="Wind", Path="Erudition")
        db.session.add(Anaxa)
        Anaxa.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd])

        # The Remembrance
        Aglaea = Character(Name="Aglaea", Role="DPS", Element="Lightning", Path="Remembrance")
        db.session.add(Aglaea)
        Aglaea.Needs.extend([need_atk, need_critDMG, need_critRATE, need_DMG, need_spd, need_energyRegen])

        Castorice = Character(Name="Castorice", Role="DPS", Element="Quantum", Path="Remembrance")
        db.session.add(Castorice)
        Castorice.Needs.extend([need_hp, need_critDMG, need_critRATE, need_DMG])

        Evernight = Character(Name="Evernight", Role="DPS", Element="Ice", Path="Remembrance")
        db.session.add(Evernight)
        Evernight.Needs.extend([need_hp, need_critDMG, need_critRATE, need_DMG, need_spd])

        # The Nihility
        Kafka = Character(Name="Kafka", Role="DPS", Element="Lightning", Path="Nihility")
        db.session.add(Kafka)
        Kafka.Needs.extend([need_atk, need_DMG, need_spd])

        Welt = Character(Name="Welt", Role="DPS", Element="Imaginary", Path="Nihility")
        db.session.add(Welt)
        Welt.Needs.extend([need_atk, need_DMG, need_spd, need_critDMG, need_critRATE])

        BlackSwan = Character(Name="Black Swan", Role="DPS", Element="Wing", Path="Nihility")
        db.session.add(BlackSwan)
        BlackSwan.Needs.extend([need_atk, need_DMG, need_spd])

        Acheron = Character(Name="Acheron", Role="DPS", Element="Lightning", Path="Nihility")
        db.session.add(Acheron)
        Acheron.Needs.extend([need_atk, need_DMG, need_spd, need_critDMG, need_critRATE])

        Cipher = Character(Name="Cipher", Role="DPS", Element="Quantum", Path="Nihility")
        db.session.add(Cipher)
        Cipher.Needs.extend([need_atk, need_DMG, need_spd, need_critDMG, need_critRATE])

        Hysilens = Character(Name="Acheron", Role="DPS", Element="Physical", Path="Nihility")
        db.session.add(Hysilens)
        Hysilens.Needs.extend([need_atk, need_DMG, need_spd])

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

        Hyacine = Character(Name="Hyacine", Role="Sustain", Element="Wind", Path="Rememberance")
        db.session.add(Hyacine)

        # The Abudance 
        
        Bailu = Character(Name="Bailu", Role="Sustain", Element="Lightning", Path="Abudance")
        db.session.add(Bailu)

        Luocha = Character(Name="Luocha", Role="Sustain", Element="Imaginary", Path="Abudance")
        db.session.add(Luocha)

        Huohuo = Character(Name="Huohuo", Role="Sustain", Element="Wind", Path="Abudance")
        db.session.add(Huohuo)

        Lingsha = Character(Name="Lingsha", Role="Sustain", Element="Fire", Path="Abudance")
        db.session.add(Lingsha)

        # ====================================
        # 3. SKILLS
        # ====================================
        skill1_bronya = Skill(Name="Combat Redeployment", Description="Boosts ally ATK and advances their action.", CharacterName="Bronya")
        skill2_bronya = Skill(Name="The Belobog March", Description="Provides team-wide damage buff.", CharacterName="Bronya")
        skill1_sunday = Skill(Name="Benison of Paper and Rites", Description="Boosts ally DMG, CritRate and advances their action.", CharacterName="Sunday")
        skill2_sunday = Skill(Name="Ode to Caress and Cicatrix", Description="Regenerates ally energy and increases CritDMG", CharacterName="Sunday")
        db.session.add_all([skill1_bronya, skill2_bronya, skill1_sunday, skill2_sunday])

        # ====================================
        # 4. EFFECTS
        # ====================================
        eff_atk_49 = Effect(Name="ATK%", Value=49)
        eff_critdmg_33 = Effect(Name="CRITDMG%", Value=33)
        eff_dmg_58 = Effect(Name="DMG%", Value=58)
        eff_dmg_69 = Effect(Name="DMG%", Value=69)
        eff_critdmg_37 = Effect(Name="CRITDMG%", Value=37)
        eff_critrate_18 = Effect(Name="CRITRATE%", Value=18)
        db.session.add_all([eff_atk_49, eff_critdmg_33, eff_dmg_58, eff_dmg_69, eff_critdmg_37, eff_critrate_18])

        # ====================================
        # 5. Przypisanie efektow do skillow
        # ====================================
        skill1_bronya.Effects.extend([eff_dmg_58])
        skill2_bronya.Effects.extend([eff_critdmg_33, eff_atk_49])
        skill1_sunday.Effects.extend([eff_dmg_69, eff_critrate_18])
        skill2_sunday.Effects.extend([eff_critdmg_37])

        # ====================================
        # 6. Commit wszystkich zmian
        # ====================================
        db.session.commit()
        print("CHAR AFTER:", Character.query.count())  # test po seedzie
        print("SEED COMPLETE")

if __name__ == "__main__":
    run_seed()
