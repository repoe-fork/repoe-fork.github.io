from typing import Any, Dict, Optional

from PyPoE.poe.file.dat import DatRecord

from RePoE.parser import Parser_Module
from RePoE.parser.util import call_with_default_args, get_release_state, write_any_json


def _convert_base_item_specific(
        base_item_type: Optional[DatRecord], obj: Dict[str, Any]
) -> None:
    if base_item_type is None:
        obj["base_item"] = None
        return

    obj["base_item"] = {
        "id": base_item_type["Id"],
        "display_name": base_item_type["Name"],
        "release_state": get_release_state(base_item_type["Id"]).name,
    }


def convert_gem(
        skill_gem: DatRecord,
        gem_effect: DatRecord,
) -> Dict[str, Any]:
    obj = {}

    gem_tags = gem_effect["GemTags"]
    if gem_tags:
        obj["tags"] = [tag["Id"] for tag in gem_tags]

    obj["gem_type"] = ["active", "support", "spirit"][skill_gem["GemType"]]

    obj["color"] = [None, "r", "g", "b", "w"][skill_gem["GemColour"]]

    obj["requirement_weights"] = {attr.lower(): skill_gem[f"{attr}RequirementPercent"]
                                  for attr in ["Strength", "Dexterity", "Intelligence"]}

    obj["grants_skills"] = [s["Id"] for s in [gem_effect["GrantedEffect"]]
                            + gem_effect["AdditionalGrantedEffects"]]

    _convert_base_item_specific(skill_gem["BaseItemType"], obj)

    obj["support_name"] = gem_effect["SupportName"] or None
    obj["support_text"] = gem_effect["SupportText"] or None
    obj["skill_name"] = gem_effect["Name"] or None

    obj["crafting_types"] = [t["Name"] for t in skill_gem["CraftingTypes"]] or None
    obj["crafting_level"] = skill_gem["CraftingLevel"]

    obj["tutorial_video"] = skill_gem["TutorialVideo"] or None
    obj["ui_image"] = skill_gem["UI_Image"] or None

    return obj


class skill_gems(Parser_Module):
    def write(self) -> None:
        skill_gems = []
        relational_reader = self.relational_reader

        # Skills from gems
        for gem in relational_reader["SkillGems.dat64"]:
            for gem_effect in gem["GemEffects"]:
                if (
                        (gem_effect["Name"] and ("[DNT]" in gem_effect["Name"])) or
                        (gem_effect["ItemColor"] != 3 and gem["IsVaalVariant"])
                ):
                    continue

                skill_gems.append(convert_gem(gem, gem_effect))

        write_any_json(skill_gems, self.data_path, "skill_gems")


if __name__ == "__main__":
    call_with_default_args(skill_gems)
