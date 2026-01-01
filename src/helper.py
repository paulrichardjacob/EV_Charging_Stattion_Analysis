import numpy as np

class Helper:
    @staticmethod
    def iqr(series):
        """
        Calculate lower and upper bounds for outlier detection
        using the Interquartile Range (IQR) method.
        """
        series = np.asarray(series)
        series = series[~np.isnan(series)]

        if len(series) == 0:
            return None, None

        Q1 = np.percentile(series, 25)
        Q3 = np.percentile(series, 75)
        IQR = Q3 - Q1

        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)

        return lower_bound, upper_bound
