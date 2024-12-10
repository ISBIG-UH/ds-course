SELECT IdS, COVAR_SAMP(WIND, precipitation) AS CovarianzaVientoPrecipitacion
FROM Lectura_Aire
JOIN Lectura ON Lectura_Aire.IdL = Lectura.IdL
JOIN Lectura_Precipitaciones ON Lectura_Aire.IdL = Lectura_Precipitaciones.IdL
GROUP BY IdS;
