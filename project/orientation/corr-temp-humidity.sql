SELECT IdS, sys.CORR(SOIL_TEMPERATURE, RELATIVE_HUMIDITY) AS CorrelacionTemperaturaHumedad
FROM Lectura_Temperatura
JOIN Lectura ON Lectura_Temperatura.IdL = Lectura.IdL
JOIN Lectura_Humedad ON Lectura_Temperatura.IdL = Lectura_Humedad.IdL
GROUP BY IdS;
