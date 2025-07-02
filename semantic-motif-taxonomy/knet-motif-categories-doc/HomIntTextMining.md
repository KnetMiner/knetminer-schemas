

# Class: Text Mining Annotation about Homology Interaction (HomIntTextMining) 


_An association that represents a text mining annotation based on homology interaction._

__





URI: [motif:HomIntTextMining](https://knetminer.com/terms/motifs/motif-categories/HomIntTextMining)






```mermaid
 classDiagram
    class HomIntTextMining
    click HomIntTextMining href "../HomIntTextMining"
      TextMiningAnnotation <|-- HomIntTextMining
        click TextMiningAnnotation href "../TextMiningAnnotation"
      HomologyInteraction <|-- HomIntTextMining
        click HomologyInteraction href "../HomologyInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [Homology](Homology.md) [ [CrossSpecieAssociation](CrossSpecieAssociation.md)]
                * [HomologyInteraction](HomologyInteraction.md)
                    * **HomIntTextMining** [ [TextMiningAnnotation](TextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:HomIntTextMining |
| native | motif:HomIntTextMining |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomIntTextMining
description: 'An association that represents a text mining annotation based on homology
  interaction.

  '
title: Text Mining Annotation about Homology Interaction
notes:
- 'original category: 5.3'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: HomologyInteraction
mixins:
- TextMiningAnnotation

```
</details>

### Induced

<details>
```yaml
name: HomIntTextMining
description: 'An association that represents a text mining annotation based on homology
  interaction.

  '
title: Text Mining Annotation about Homology Interaction
notes:
- 'original category: 5.3'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: HomologyInteraction
mixins:
- TextMiningAnnotation

```
</details>