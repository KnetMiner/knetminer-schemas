

# Class: Text Mining Annotation about Gene-Gene Interaction (GeneIntTextMining) 


_An association that represents a text mining annotation based on gene-gene interaction._

__





URI: [motif:GeneIntTextMining](https://knetminer.com/terms/motifs/motif-categories/GeneIntTextMining)






```mermaid
 classDiagram
    class GeneIntTextMining
    click GeneIntTextMining href "../GeneIntTextMining"
      TextMiningAnnotation <|-- GeneIntTextMining
        click TextMiningAnnotation href "../TextMiningAnnotation"
      GeneGeneInteraction <|-- GeneIntTextMining
        click GeneGeneInteraction href "../GeneGeneInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [GeneGeneInteraction](GeneGeneInteraction.md)
            * **GeneIntTextMining** [ [TextMiningAnnotation](TextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategory | interaction::genetic::literature |




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
  originalCategory:
    tag: originalCategory
    value: interaction::genetic::literature
description: 'An association that represents a text mining annotation based on gene-gene
  interaction.

  '
title: Text Mining Annotation about Gene-Gene Interaction
notes:
- 'original category no: 2.11'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneGeneInteraction
mixins:
- TextMiningAnnotation

```
</details>

### Induced

<details>
```yaml
name: GeneIntTextMining
annotations:
  originalCategory:
    tag: originalCategory
    value: interaction::genetic::literature
description: 'An association that represents a text mining annotation based on gene-gene
  interaction.

  '
title: Text Mining Annotation about Gene-Gene Interaction
notes:
- 'original category no: 2.11'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: GeneGeneInteraction
mixins:
- TextMiningAnnotation

```
</details>