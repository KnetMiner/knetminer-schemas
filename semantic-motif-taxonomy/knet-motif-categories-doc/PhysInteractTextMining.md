

# Class: Physical Interaction Text Mining (PhysInteractTextMining) 


_A text mining annotation about on physical interaction._

__





URI: [motif:PhysInteractTextMining](https://knetminer.com/terms/motifs/motif-categories/PhysInteractTextMining)






```mermaid
 classDiagram
    class PhysInteractTextMining
    click PhysInteractTextMining href "../PhysInteractTextMining"
      HasTextMiningAnnotation <|-- PhysInteractTextMining
        click HasTextMiningAnnotation href "../HasTextMiningAnnotation"
      PhysicalInteraction <|-- PhysInteractTextMining
        click PhysicalInteraction href "../PhysicalInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BioMolecularInteraction](BioMolecularInteraction.md)
        * [PhysicalInteraction](PhysicalInteraction.md)
            * **PhysInteractTextMining** [ [HasTextMiningAnnotation](HasTextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | interaction::physical::literature |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:PhysInteractTextMining |
| native | motif:PhysInteractTextMining |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysInteractTextMining
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::physical::literature
description: 'A text mining annotation about on physical interaction.

  '
title: Physical Interaction Text Mining
notes:
- 'original category no: 2.8'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: PhysicalInteraction
mixins:
- HasTextMiningAnnotation

```
</details>

### Induced

<details>
```yaml
name: PhysInteractTextMining
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::physical::literature
description: 'A text mining annotation about on physical interaction.

  '
title: Physical Interaction Text Mining
notes:
- 'original category no: 2.8'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: PhysicalInteraction
mixins:
- HasTextMiningAnnotation

```
</details>