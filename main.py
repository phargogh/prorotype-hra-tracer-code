def main():
    pass

    # TODO: how to handle spatially explicit criteria?

    # workflow:
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
    #       calculate pairwise exposure, consequence from:
    #           * habitat/stressor parameters
    #           * EDT of the stressor and buffer distance
    #           * The habitat raster
    #           --> The calculation will only happen for habitat pixels that are within the
    #           buffer distance of the stressor in question.
    #           --> Once calculated, the numerator is multiplied by the EDT-derived decay
    #           function.  Thus, stressors overlapping a habitat have larger
    #           values, and habitat pixels some distance away from stressors
    #           will have very small or 0 scores from this stressor.
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



if __name__ == '__main__':
    main()
