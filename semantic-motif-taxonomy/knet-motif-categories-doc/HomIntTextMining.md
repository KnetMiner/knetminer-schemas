

# Class: Homology Interaction Text Mining (HomIntTextMining) 


_An association that represents a text mining annotation based on homology and interaction._

__





URI: [motif:HomIntTextMining](https://knetminer.com/terms/motifs/motif-categories/HomIntTextMining)






```mermaid
 classDiagram
    class HomIntTextMining
    click HomIntTextMining href "../HomIntTextMining"
      HasTextMiningAnnotation <|-- HomIntTextMining
        click HasTextMiningAnnotation href "../HasTextMiningAnnotation"
      HomologyInteraction <|-- HomIntTextMining
        click HomologyInteraction href "../HomologyInteraction"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [HomologyInteraction](HomologyInteraction.md)
        * **HomIntTextMining** [ [HasTextMiningAnnotation](HasTextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategories | homint::literature |




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
annotations:
  originalCategories:
    tag: originalCategories
    value: homint::literature
description: 'An association that represents a text mining annotation based on homology
  and interaction.

  '
title: Homology Interaction Text Mining
notes:
- 'original category no: 5.3'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: HomologyInteraction
mixins:
- HasTextMiningAnnotation

```
</details>

### Induced

<details>
```yaml
name: HomIntTextMining
annotations:
  originalCategories:
    tag: originalCategories
    value: homint::literature
description: 'An association that represents a text mining annotation based on homology
  and interaction.

  '
title: Homology Interaction Text Mining
notes:
- 'original category no: 5.3'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: HomologyInteraction
mixins:
- HasTextMiningAnnotation

```
</details>