from __init__ import create_app
from extensions import db

from models.Character import Character, Character_Need
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
        db.session.add_all([need_atk, need_critDMG, need_critRATE, need_spd, need_hp, need_DMG])

        # ====================================
        # 2. CHARACTERS
        # ====================================
        Seele = Character(Name="Seele", Role="DPS", Element="Quantum", Path="Hunt")
        db.session.add(Seele)
        Seele.Needs.extend([need_atk, need_critDMG, need_critRATE, need_spd])

        Bronya = Character(Name="Bronya", Role="Support", Element="Wind", Path="Harmony")
        db.session.add(Bronya)

        Sunday = Character(Name="Sunday", Role="Support", Element="Imaginary", Path="Harmony")
        db.session.add(Sunday)

        Gepard = Character(Name="Gepard", Role="Sustain", Element="Ice", Path="Preservation")
        db.session.add(Gepard)

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
