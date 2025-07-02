

# Class: Gene-to-Trait Association via Physical Interaction (PhysInteractTraitAssn) 


_A gene-to-trait association based on physical interaction._

__





URI: [motif:PhysInteractTraitAssn](https://knetminer.com/terms/motifs/motif-categories/PhysInteractTraitAssn)






```mermaid
 classDiagram
    class PhysInteractTraitAssn
    click PhysInteractTraitAssn href "../PhysInteractTraitAssn"
      Gene2TraitAssociation <|-- PhysInteractTraitAssn
        click Gene2TraitAssociation href "../Gene2TraitAssociation"
      PhysicalInteraction <|-- PhysInteractTraitAssn
        click PhysicalInteraction href "../PhysicalInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [PhysicalInteraction](PhysicalInteraction.md)
            * **PhysInteractTraitAssn** [ [Gene2TraitAssociation](Gene2TraitAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:PhysInteractTraitAssn |
| native | motif:PhysInteractTraitAssn |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysInteractTraitAssn
description: 'A gene-to-trait association based on physical interaction.

  '
title: Gene-to-Trait Association via Physical Interaction
notes:
- 'original category: 2.7'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: PhysicalInteraction
mixins:
- Gene2TraitAssociation

```
</details>

### Induced

<details>
```yaml
name: PhysInteractTraitAssn
description: 'A gene-to-trait association based on physical interaction.

  '
title: Gene-to-Trait Association via Physical Interaction
notes:
- 'original category: 2.7'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: PhysicalInteraction
mixins:
- Gene2TraitAssociation

```
</details>