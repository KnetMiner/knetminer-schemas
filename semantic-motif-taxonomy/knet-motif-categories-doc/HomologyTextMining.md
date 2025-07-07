

# Class: Text Mining Annotation about Homology (HomologyTextMining) 


_An association that represents a text mining annotation based on homology._

__





URI: [motif:HomologyTextMining](https://knetminer.com/terms/motifs/motif-categories/HomologyTextMining)






```mermaid
 classDiagram
    class HomologyTextMining
    click HomologyTextMining href "../HomologyTextMining"
      TextMiningAnnotation <|-- HomologyTextMining
        click TextMiningAnnotation href "../TextMiningAnnotation"
      Homology <|-- HomologyTextMining
        click Homology href "../Homology"
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * [BiologicalTopic](BiologicalTopic.md)
        * [Phylogeny](Phylogeny.md)
            * [Homology](Homology.md) [ [CrossSpecieAssociation](CrossSpecieAssociation.md)]
                * **HomologyTextMining** [ [TextMiningAnnotation](TextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| associationStrength | 3.3 |
| originalCategory | phylogeny::homology::literature |




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
  associationStrength:
    tag: associationStrength
    value: 3.3
  originalCategory:
    tag: originalCategory
    value: phylogeny::homology::literature
description: 'An association that represents a text mining annotation based on homology.

  '
title: Text Mining Annotation about Homology
notes:
- 'original category no: 3.3'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- TextMiningAnnotation

```
</details>

### Induced

<details>
```yaml
name: HomologyTextMining
annotations:
  associationStrength:
    tag: associationStrength
    value: 3.3
  originalCategory:
    tag: originalCategory
    value: phylogeny::homology::literature
description: 'An association that represents a text mining annotation based on homology.

  '
title: Text Mining Annotation about Homology
notes:
- 'original category no: 3.3'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: Homology
mixins:
- TextMiningAnnotation

```
</details>