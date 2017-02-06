import argparse
import vcf
import numpy as np
import pandas as pd
from chart_plotter import ChartPlotter
from sklearn.cluster import MeanShift, estimate_bandwidth

class MosaicClusterer():

#read in VCF containing filtered variants
   def read_vcf(vcf_file):
     vcf_reader = vcf.Reader(open(vcf_file))
     variants = []
     for record in vcf_reader:
        if len(record.get_hets()) > 0:
        	 variants.append(record)
     
     return variants
     
   def extract_allele_depths(records):
      ref_allele_depths = []
      alt_allele_depths = []
      gq_scores = []
      
      for variant in htz_variants:
         for sample in variant.samples:
            print(sample)
            ref_allele_depths.append(sample['AD'][0]) 
            alt_allele_depths.append(sample['AD'][1])
            gq_scores.append(sample['GQ'])
      allele_depths = np.array([ref_allele_depths, alt_allele_depths, gq_scores])     
      return allele_depths
      
   def calculate_mean_shift(allele_depths, this_quantile):
      number_of_samples = len(allele_depths[0])
      
      allele_depth_array = np.array(allele_depths)
      allele_depth_transposed_array = np.transpose(allele_depth_array)
      
      bandwidth = estimate_bandwidth(allele_depth_transposed_array, quantile=this_quantile, n_samples=number_of_samples)
      
      ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
      ms.fit(allele_depth_transposed_array)
      return [allele_depth_transposed_array, ms]
      
           
#cluster variants by AD using MeanShift
#output variants with assigned cluster

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Mosaic Clusterer')
   parser.add_argument('vcf_file', help='Valid VCF file to process' )
   args = parser.parse_args()
   
   mosaic_clusterer = MosaicClusterer
   htz_variants = mosaic_clusterer.read_vcf(args.vcf_file)
   allele_depths = mosaic_clusterer.extract_allele_depths(htz_variants)
   results = mosaic_clusterer.calculate_mean_shift(allele_depths, 0.6)

   chart_plotter = ChartPlotter
   chart_plotter.render(results[0], results[1])

