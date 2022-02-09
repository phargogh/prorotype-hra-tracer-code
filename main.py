def main():
    pass

    # TODO: how to handle spatially explicit criteria?

    # Current (3.10.1) workflow:
    #
    # Align inputs to the AOI
    # Rasterize the AOI.
    #  * If there's only 1 unique "name" attribute value, rasterize whole AOI
    #    onto one raster
    #  * If there are multiple unique "name" attribute values, group the
    #    unique sets of "name" features onto 1 raster layer per unique "name".
    #  -->  NOTE that after the AOI is rasterized, it is only used for zonal
    #       stats
    #
    # For each spatial input:
    #   If the input is already a raster, just get the path for alignment.
    #   Convert all input vectors to rasters by simplifying and rasterizing.
    #       * Spatial criteria should have their rating field burned in.
    #       * habitat/stressor vectors have presence (1) / absence (nodata)
    #         burned in
    #
    # Align the whole stack of spatial rasters
    #   * Reproject to the AOI projetion
    #   * Union of bboxes.
    #
    # For each stressor:
    #   * Do an EDT
    #
    # Count the number of habitats on each pixel.
    #
    # For each habitat
    #    Calculate habitat recovery
    #
    #    For each stressor
    #       calculate the pairwise exposure score
    #       calculate the pairwise consequence score
    #       calculate the pairwise risk score from exposure, consequence
    #       reclassify pairwise risk into high/med/low
    #
    #    Calculate the cumulative exposure
    #    Calculate the cumulative consequence
    #    Calculate the cumulative risk for this habitat
    #    Reclassify risk to habitat
    #
    # Compute total risk to the ecosystem
    # Reclassify the ecosystem risk.
    #
    # Do zonal statistics

    # TODO: move pandas-based paths into the execute function
    # TODO: replace _get_vector_geometries_by_field with OGRSQL
    # TODO: Look at _tot_recovery_op -- normalizing which it should not?

    # What I think the workflow can become.
    #
    # Data Prep:
    #   * Simplify the AOI and rasterize
    #   * For each habitat/stressor file:
    #       * Simplify and rasterize.
    #       * If a stressor, do an EDT and mask to the buffer distance.
    #   * For each criterion:
    #       * if the criterion is a spatial raster, do nothing.
    #       * if the criterion is a spatial vector, simplify and rasterize
    #       * if the criterion is numeric, keeping as a number would save disk
    #         accesses, making a new raster might allow for a cleaner
    #         implementation.  TODO: pick an approach
    #   * Align the stack of spatial inputs, taking the bbox union,
    #     reprojecting to the AOI.
    #
    # Count the number of habitats overlapping on a pixel
    # Count the number of stressors overlapping on a pixel
    #
    # For each habitat:
    #   Calculate habitat recovery
    #
    #   For each stressor:
    #       * Calculate the pairwise exposure score
    #       * Calculate the pairwise consequence score
    #       * given pairwise exposure, consequence scores, calculate risk
    #       * reclassify pairwise risk into high/med/low
    #
    #   Calculate cumulative exposure
    #   Calculate cumulative consequence
    #   Calculate cumulative risk for this habitat
    #   Reclassify risk to habitat
    #
    # Compute total risk to the ecosystem
    # Reclassify the total ecosystem risk
    #
    # Do zonal statistics.
    # If requested, create geojson outputs for visualization.


if __name__ == '__main__':
    main()
