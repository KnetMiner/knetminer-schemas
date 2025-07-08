

# Class: Physical Interaction-related Association (PhysicalInteraction) 


_Associations of this type are related to physical interactions between genes, proteins or other _

_biomolecular entities._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:PhysicalInteraction](https://knetminer.com/terms/motifs/motif-categories/PhysicalInteraction)






```mermaid
 classDiagram
    class PhysicalInteraction
    click PhysicalInteraction href "../PhysicalInteraction"
      BiologicalTopic <|-- PhysicalInteraction
        click BiologicalTopic href "../BiologicalTopic"
      

      PhysicalInteraction <|-- PhysInteractManualAnn
        click PhysInteractManualAnn href "../PhysInteractManualAnn"
      PhysicalInteraction <|-- PhysInteractTraitAssn
        click PhysInteractTraitAssn href "../PhysInteractTraitAssn"
      PhysicalInteraction <|-- PhysInteractTextMining
        click PhysInteractTextMining href "../PhysInteractTextMining"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * **PhysicalInteraction**
            * [PhysInteractManualAnn](PhysInteractManualAnn.md) [ [ManualAnnotationMethod](ManualAnnotationMethod.md)]
            * [PhysInteractTraitAssn](PhysInteractTraitAssn.md) [ [Gene2TraitAssociation](Gene2TraitAssociation.md)]
            * [PhysInteractTextMining](PhysInteractTextMining.md) [ [TextMiningAnnotationMethod](TextMiningAnnotationMethod.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:PhysicalInteraction |
| native | motif:PhysicalInteraction |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysicalInteraction
description: "Associations of this type are related to physical interactions between\
  \ genes, proteins or other \nbiomolecular entities.\n"
title: Physical Interaction-related Association
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: BiologicalTopic
abstract: true

```
</details>

### Induced

<details>
```yaml
name: PhysicalInteraction
description: "Associations of this type are related to physical interactions between\
  \ genes, proteins or other \nbiomolecular entities.\n"
title: Physical Interaction-related Association
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: BiologicalTopic
abstract: true

```
</details>