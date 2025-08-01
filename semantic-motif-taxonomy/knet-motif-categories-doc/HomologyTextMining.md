

# Class: Homology Text Mining (HomologyTextMining) 


_An association that represents a text mining annotation based on homology._

__





URI: [motif:HomologyTextMining](https://knetminer.com/terms/motifs/motif-categories/HomologyTextMining)






```mermaid
 classDiagram
    class HomologyTextMining
    click HomologyTextMining href "../HomologyTextMining"
      HasTextMiningAnnotation <|-- HomologyTextMining
        click HasTextMiningAnnotation href "../HasTextMiningAnnotation"
      Homology <|-- HomologyTextMining
        click Homology href "../Homology"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [PhylogenyConfidentAssociation](PhylogenyConfidentAssociation.md)
        * [Homology](Homology.md) [ [CrossSpeciesAssociation](CrossSpeciesAssociation.md)]
            * **HomologyTextMining** [ [HasTextMiningAnnotation](HasTextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| originalCategories | phylogeny::homology::literature |




### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:HomologyTextMining |
| native | motif:HomologyTextMining |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomologyTextMining
annotations:
  originalCategories:
    tag: originalCategories
    value: phylogeny::homology::literature
description: 'An association that represents a text mining annotation based on homology.

  '
title: Homology Text Mining
notes:
- 'original category no: 3.3'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- HasTextMiningAnnotation

```
</details>

### Induced

<details>
```yaml
name: HomologyTextMining
annotations:
  originalCategories:
    tag: originalCategories
    value: phylogeny::homology::literature
description: 'An association that represents a text mining annotation based on homology.

  '
title: Homology Text Mining
notes:
- 'original category no: 3.3'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- HasTextMiningAnnotation

```
</details>