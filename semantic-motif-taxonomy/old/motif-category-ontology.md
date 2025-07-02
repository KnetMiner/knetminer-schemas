# KnetMiner Semantic Motif Association Ontology


```yaml
Semantic Motif Category:

	Association Strength:
		Intra-Specie Association:
		  # has children in Biological Topic, see below
			# original: Tier 1 and Tier 2
		Cross-Specie Association:
		Computationally Inferred Association:
			Text Mining:
			  # Inferred from literature with methods like text mining
				# Original name: Literature
		Sequence Similarity:
		  # TODO: are sub-categories Intra-Specie, Cross-Specie, or can they be either?

	Biological Topic:
	  # The kind of biological phenomenon or experimental technique that is 
		# used to provide evidence for a gene/entity association
	  Gene-to-Phenotype:
      # Gene is causally associated to a phenotype
			# Original name: genetics
			Gene-to-Trait:
			  # Added as a subclass, in case you want to be more specific on the kind of phenotype
				# you're talking about
			  # Original name: genetics
				Intra.Trait:
				  label: Intra-Specie Gene to Trait association
					other parents:
					  - Intra-Specie Association
					# original: 1.2
		Gene Expression:
		  other parents:
				# Since they're all in tier 2 and this is described as intra-specie, we subclass
				# this here.
				# TODO: we might need a different branch if we expect these categories to 
				# be used both intra- and cross-specie (which, in principle, makes sense).
				# Note that this makes all the children below to fall under Intra-Specie too.
				# Original name: expression
				# original: Tier 2
			  - Intra-Specie Association
		  Differential Expression:
			  # original: 2.1
			Co-Expression:
			  # original: 2.2
			Expression Regulation:
			  Regulation.Manual:
				  label: Manual Annotation about Gene Expression Regulation
					# original: 2.3
					other parents:
					  - Manual Annotation
				Regulation.Trait:
				  label: Gene-to-Trait Association via Gene Expression Regulation
				  # original: 2.4
					other parents:
					  - Gene-to-Trait
				Regulation.Text Mining:
				  label: Text Mining about Gene Expression Regulation
					# original: 2.5
					other parents:
					  - Text Mining
		Physical Interaction:
		  # original name: interaction::physical
			PhysInteract.Manual:
        label: Manual Annotation about Phyical Interaction
				# original: 2.6
				other parents:
				  - Manual Annotation
			PhysInteract.Trait:
			  label: Gene-to-Trait Association via Physical Interaction
				# original: 2.7
			PhysInteract.Text Mining:
			  label: Text Mining about Physical Interaction
				# original: 2.8
				other parents:
				  - Text Mining
		Gene-Gene Interaction:
		  # original name: interaction::genetic
			# In the traverser config, motifs in this category seem to track 
			# gene2gene interactions, so I propose this new name
			GeneInt.Manual:
			  label: Manual Annotation about Gene-to-Gene Interaction
				# original: 2.9
				other parents:
				  - Manual Annotation
			GeneInt.Trait:
			  label: Gene-to-Trait Association via Gene-to-Gene Interaction
				# original 2.10
				other parents:
				  - Gene-to-Trait
			GeneInt.Text Mining:
			  label: Text Mining about via Gene-to-Gene Interaction
				# original 2.11
				other parents:
				  - Text Mining
		Phylogeny:
		  Homoeology:
			  other parents:
				  - Intra-Specie Association # because that's the meaning of homoeology
				Homoeology.Manual:
				  label: Manual Annotation about Homoeology
					# original: 3.4
					other parents:
					  - Manual Annotation
				Homoeology.Trait:
				  label: Gene-to-Trait Association via Homoeology
					# original: 3.5
					other parents:
					  - Gene-to-Trait
				Homoeology.Text Mining:
				  label: Text Mining about Homoeology
					# original 3.6
					other parents:
					  - Text Mining					
			Homology:
			  other parents:
				  - Cross-Specie Association # because that's the meaning of homology
				Homology.Manual:
				  label: Manual Annotation about Homology
					# original: 3.1
					other parents:
					  - Manual Annotation
				Homology.Trait:
				  label: Gene-to-Trait Association via Homology
					# original: 3.2
					other parents:
					  - Gene-to-Trait
				Homology.Text Mining:
				  label: Text Mining about Homology
					# original 3.3
					other parents:
					  - Text Mining
				Homology Interaction:
				  # original: Tier 5
				  # note that cross-specie is inherited from the parent
					HomInt.Manual:
						label: Manual Annotation about Homology Interaction
						# original: 5.1
						other parents:
							- Manual Annotation
					HomInt.Trait:
						label: Gene-to-Trait Association via Homology Interaction
						# original: 5.2
						other parents:
							- Gene-to-Trait
					HomInt.Text Mining:
						label: Text Mining about Homology Interaction
						# original 5.3
						other parents:
							- Text Mining
			Sequence Similarity:
			  other parents:
				  - Association Strength
				SeqSim.Manual:
				  label: Manual Annotation about Sequence Similarity
					# original: 4.1
					other parents:
					  - Manual Annotation
				SeqSim.Trait:
				  label: Gene-to-Trait Association via Sequence Similarity
					# original: 4.2
					other parents:
					  - Gene-to-Trait

  Annotation Method:
	  Manual Annotation:
		  Intra.Manual:
			  label: Intra-Specie Manual Annotation
				# original: 1.1
				other parents:
				  - Intra-Specie Association
	  Text mining:
		  # this falls into this strength category via multiple inheritance
		  other parents:
			  - Computationally Inferred
		  Intra-Specie Text Mining:
			  label: Intra-Specie Text Mining Annotation
				other parents:
				  - Intra-Specie Association
				# original: 1.3
		
    
```


## Tier 1

The general category here is LINK STRENGTH (STRENGTH in the follow), with 2 major classes:
* Intra-specie Intra
  * Intra-specie and inferred InfIntra
* Cross-specie XS
  * Cross-specie and inferred InfXS

1.1) Intra ASSERTION METHOD Manual Annot
1.2) Intra BIOLOGICAL TOPIC Gene association to Trait (TraitAss)
1.3) Intra ASSERTION METHOD Inferred from literature


## Tier 2

STRENGTH Intra
BIO TOPIC Gene Expression or physical interactions

2.1 TOPIC Diff Expression
2.2 TOPIC Co-expression
2.3 TOPIC Expression Regulation, METHOD Manual Annot
2.4 TOPIC TraitAss by Expr Regulation (ie, 2 topics)
2.5 TOPIC Exp Reg METHOD Inferred from literature
2.6 TOPIC Physical Interaction METHOD Manual Annot
2.7 TOPIC TraitAss by Physical Interaction 
2.8 TOPIC TraitAss by Physical Interaction METHOD Inferred from Literature

2.9-2.11 interaction::genetic looks like gene-gene association due to genetic (or other?) reasons => TOPIC Gene-Gene association (Gene2Gene)

2.9 TOPIC Gene2Gene METHOD Manual Annot
2.10 TOPIC TraitAss by Gene2Gene
2.11 TOPIC Gene2Gene METHOD Inferred from Literature


## Tier 3

Phylogeny is top TOPIC, with subtopics:

Homoeology is TOPIC and STRENGTH Intra-Specie
Homology is TOPIC and STRENGTH Cross-Specie

3.1 TOPIC Homology METHOD Manual
3.2 TOPIC TraitAss by Homology
3.3 TOPIC Homology METHOD Literature
3.4 TOPIC Homoeology METHOD Manual
3.5 ...
3.6 ...

## Tier 4

Sequence Similarity is both a TOPIC and STRENGTH
it's subtopic of Philogeny

4.1 SeqSim METHOD Manual
4.2 SeqSim METHOD Literature

## Tier 5

Homology Interaction is a TOPIC under Homology
and it is a STRENGTH under Cross-Specie

5.1 TOPIC Hom Int METHOD Manual
5.2 TraitAss by HomInt
5.3 HomInt METHOD Literature
