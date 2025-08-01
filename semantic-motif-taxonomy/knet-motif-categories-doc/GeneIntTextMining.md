

# Class: Gene-Gene Interaction Text Mining (GeneIntTextMining) 


_An association that represents a text mining annotation based on gene-gene interaction._

__





URI: [motif:GeneIntTextMining](https://knetminer.com/terms/motifs/motif-categories/GeneIntTextMining)






```mermaid
 classDiagram
    class GeneIntTextMining
    click GeneIntTextMining href "../GeneIntTextMining"
      HasTextMiningAnnotation <|-- GeneIntTextMining
        click HasTextMiningAnnotation href "../HasTextMiningAnnotation"
      GeneGeneInteraction <|-- GeneIntTextMining
        click GeneGeneInteraction href "../GeneGeneInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BioMolecularInteraction](BioMolecularInteraction.md)
        * [GeneGeneInteraction](GeneGeneInteraction.md)
            * **GeneIntTextMining** [ [HasTextMiningAnnotation](HasTextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategories | interaction::genetic::literature |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:GeneIntTextMining |
| native | motif:GeneIntTextMining |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneIntTextMining
annotations:
  originalCategories:
    tag: originalCategories
    value: interaction::genetic::literature
description: 'An association that represents a text mining annotation based on gene-gene
  interaction.

  '
title: Gene-Gene Interaction Text Mining
notes:
- 'original category no: 2.11'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneGeneInteraction
mixins:
- HasTextMiningAnnotation

```
</details>

### Induced

<details>
```yaml
name: GeneIntTextMining
annotations:
  originalCategories:
    tag: originalCategories
    value: interaction::genetic::literature
description: 'An association that represents a text mining annotation based on gene-gene
  interaction.

  '
title: Gene-Gene Interaction Text Mining
notes:
- 'original category no: 2.11'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneGeneInteraction
mixins:
- HasTextMiningAnnotation

```
</details>