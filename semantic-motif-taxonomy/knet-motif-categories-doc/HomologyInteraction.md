

# Class: Homology Interaction (HomologyInteraction) 


_These paths rely on a multi-step hypothesis that assumes a protein-protein interaction is _

_conserved across species, adding a significant layer of uncertainty._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:HomologyInteraction](https://knetminer.com/terms/motifs/motif-categories/HomologyInteraction)






```mermaid
 classDiagram
    class HomologyInteraction
    click HomologyInteraction href "../HomologyInteraction"
      SemanticMotifCategory <|-- HomologyInteraction
        click SemanticMotifCategory href "../SemanticMotifCategory"
      

      HomologyInteraction <|-- HomIntAnn
        click HomIntAnn href "../HomIntAnn"
      HomologyInteraction <|-- HomIntTraitAssn
        click HomIntTraitAssn href "../HomIntTraitAssn"
      HomologyInteraction <|-- HomIntTextMining
        click HomIntTextMining href "../HomIntTextMining"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * **HomologyInteraction**
        * [HomIntAnn](HomIntAnn.md) [ [HasCuratedAnnotation](HasCuratedAnnotation.md)]
        * [HomIntTraitAssn](HomIntTraitAssn.md) [ [HasGeneTraitAssociation](HasGeneTraitAssociation.md)]
        * [HomIntTextMining](HomIntTextMining.md) [ [HasTextMiningAnnotation](HasTextMiningAnnotation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:HomologyInteraction |
| native | motif:HomologyInteraction |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomologyInteraction
description: "These paths rely on a multi-step hypothesis that assumes a protein-protein\
  \ interaction is \nconserved across species, adding a significant layer of uncertainty.\n"
title: Homology Interaction
notes:
- 'original category no: Tier 5'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SemanticMotifCategory
abstract: true

```
</details>

### Induced

<details>
```yaml
name: HomologyInteraction
description: "These paths rely on a multi-step hypothesis that assumes a protein-protein\
  \ interaction is \nconserved across species, adding a significant layer of uncertainty.\n"
title: Homology Interaction
notes:
- 'original category no: Tier 5'
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SemanticMotifCategory
abstract: true

```
</details>