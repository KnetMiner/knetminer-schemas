

# Class: Intra-Species Annotation (IntraSpeciesAnnotation) 


_Annotations between genes and other entities that are within the same species. These _

_includes manually curated annotations and text mining annotations._

__




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [motif:IntraSpeciesAnnotation](https://knetminer.com/terms/motifs/motif-categories/IntraSpeciesAnnotation)






```mermaid
 classDiagram
    class IntraSpeciesAnnotation
    click IntraSpeciesAnnotation href "../IntraSpeciesAnnotation"
      IntraSpeciesAssociation <|-- IntraSpeciesAnnotation
        click IntraSpeciesAssociation href "../IntraSpeciesAssociation"
      SemanticMotifCategory <|-- IntraSpeciesAnnotation
        click SemanticMotifCategory href "../SemanticMotifCategory"
      

      IntraSpeciesAnnotation <|-- CuratedAnn
        click CuratedAnn href "../CuratedAnn"
      IntraSpeciesAnnotation <|-- IntraSpeciesTextMiningAnn
        click IntraSpeciesTextMiningAnn href "../IntraSpeciesTextMiningAnn"
      IntraSpeciesAnnotation <|-- IntraTraitAnn
        click IntraTraitAnn href "../IntraTraitAnn"
      
      
      
```





## Inheritance
* [SemanticMotifCategory](SemanticMotifCategory.md)
    * **IntraSpeciesAnnotation** [ [IntraSpeciesAssociation](IntraSpeciesAssociation.md)]
        * [CuratedAnn](CuratedAnn.md) [ [HasCuratedAnnotation](HasCuratedAnnotation.md)]
        * [IntraSpeciesTextMiningAnn](IntraSpeciesTextMiningAnn.md) [ [HasTextMiningAnnotation](HasTextMiningAnnotation.md)]
        * [IntraTraitAnn](IntraTraitAnn.md) [ [HasGeneTraitAssociation](HasGeneTraitAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://knetminer.com/terms/motifs/motif-categories/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | motif:IntraSpeciesAnnotation |
| native | motif:IntraSpeciesAnnotation |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntraSpeciesAnnotation
description: "Annotations between genes and other entities that are within the same\
  \ species. These \nincludes manually curated annotations and text mining annotations.\n"
title: Intra-Species Annotation
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SemanticMotifCategory
abstract: true
mixins:
- IntraSpeciesAssociation

```
</details>

### Induced

<details>
```yaml
name: IntraSpeciesAnnotation
description: "Annotations between genes and other entities that are within the same\
  \ species. These \nincludes manually curated annotations and text mining annotations.\n"
title: Intra-Species Annotation
from_schema: https://knetminer.com/terms/motifs/motif-categories/schema
is_a: SemanticMotifCategory
abstract: true
mixins:
- IntraSpeciesAssociation

```
</details>