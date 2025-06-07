# RePoE

Repository of Path of Exile resources for tool developers. Source code available at https://github.com/repoe-fork/repoe.

## Files

Files are exported into several repositories within this github organization,
each of which can be found at the matching subdirectory within the gh-pages domain,
except the original poe1 export, which is found at the root of the subdomain,
for compatibility reasons:

 - [poe1 data export](https://repoe-fork.github.io/poe1.html) - a selection of data exported from
the game files in json format. The output data formats are specified by json schemas that can be found in
the [data-formats](https://repoe-fork.github.io/data-formats) - you should be able to generate data
structures for your preferred language using [quicktype](https://quicktype.io/) or a similar tool.
 - [poe2 data export](https://repoe-fork.github.io/poe2) - poe2 data generated in the same manner.
Uses the same data formats as the poe1 export where possible.
 - [Path of Building data export](https://repoe-fork.github.io/pob-data) - an export of data found
within PoB's source code, for both [poe1](https://repoe-fork.github.io/pob-data/poe1) and
[poe2](https://repoe-fork.github.io/pob-data/poe2). Of note is the `Uniques` subdirectory, which
is hand maintained by the Path of Building team - unique data cannot be datamined from the game files,
thus the other two exports only contain minimal information about unique items.

Web apps using provided files should link to files in the
[gh-pages](https://repoe-fork.github.io/), for better performance and caching behavior
than linking to raw files in the repository.

Note that the file formats are not final, they may change at any time, e.g. when the format
of files in the GGPK changes.

The following data is currently exported:

- `stat_translations.json`: Maps stat ids together with their values to human-readable
  text. This is the text that appears on items in-game.
- `stats.json`: Describes stat ids. Defines whether they are local and whether they
  are aliased depending on main-hand or off-hand.
- `mods.json`: Describes mod ids. Defines which items they can appear on and what
  stats with what values they have.
- `crafting_bench_options.json`: Describes master crafting options. Defines which
  masters can craft them at which level on which items.
- `npc_master.json`: Describes the master's signature mods and on which items they
  can appear.
- `gems.json`: Describes skill gems and skill gem effects only provided by mods.
- `gem_tags.json`: Simple object that contains all gem tags with their internal id as
  keys and their translation as value.
- `base_items.json`: Describes base item types. Contains information applicable to
  all item types, e.g. inventory size, item class and tags, as well as attribute
  requirements and properties.
- `tags.json`: Lists all possible item tags. These are the tags used in `base_items.json` and 
  `mods.json`.
- `item_classes.json`: Defines the item class ids and the tags added to items when they are
  Shaper/Elder items.
- `essences.json`: Describes essences. Defines the mods they spawn on items of the different
  item classes and general information like level and tier.
- `default_monster_stats.json`: Describes the stat base values of monsters at specific levels.
- `characters.json`: Describes the stat base values of the different player character classes.
- `flavour.json`: Table containing the flavour text used throughout the game.
- `fossils.json`: Describes fossils. Defines the mods they spawn, the tags they affect, and 
  auxillary effects of the fossils.
- `mod_types.json`: Describes the types of mods with sell price information and the tags
  relevant for fossil crafting.
- `cluster_jewels.json`: Describes how cluster jewels can be generated and how they influence the passive tree. 
- `cluster_jewel_notables.json`: Lists the notable and keystone passive skills that can appear on cluster jewels.
- `cost_types.json`: Defines the resource cost types used in `gems.json`.
- `active_skill_types.json`: List the active skill types used in `gems.json`.
- `uniques.json`: Lists the names and art files of unique items - this is the only information
included in the data files.

## Credits

- [Grinding Gear Games](http://www.grindinggear.com/) for [Path of Exile](https://www.pathofexile.com/).
  The contents of all `data` files obviously belong to them.
- [OmegaK2](https://github.com/OmegaK2/) for [PyPoE](https://github.com/OmegaK2/PyPoE).
- [Project PoE Wiki](poewiki.net) for updating PyPoE to handle the latest data format.
- [Path of Exile Tool Devs](https://github.com/poe-tool-dev/) for maintaining a standardised
  data schema.