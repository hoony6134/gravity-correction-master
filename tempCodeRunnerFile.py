row, col = src.index(lon, lat)
        elevation = src.read(1)[row, col]
        topographic_correction = 1.0 / (1.0 + (elevation / 1000.0) * 0.022)