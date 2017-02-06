# Mosaic Clusterer

Test scripts to investigate Mean Shift clustering with filtered VCF files containing mosaic variants.

* Call variants as normal against sample using GATK HaplotypeCaller
* Recall using GATK HaplotypeCaller with ploidy set to 5
* Filter high ploidy file agains normal VCF
* Filter to remove variants of no known medical impact and high frequency in ExAC
* Use Mosaic Clusterer to check for the clustering of mosaic variant (HTZ/HMZ)

![Mosaic variants clustered by Mean Shift](https://github.com/pasted/mosaic_clusterer/blob/master/mosaic_variants.png)
