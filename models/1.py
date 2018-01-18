# Defining hurst exponent function
def hurst(lags, timeseries):
    tau = [sqrt(std(subtract(timeseries[lag:], timeseries[:-lag]))) for lag in lags]
    hurst = polyfit(log(lags), log(tau), 1)[0] * 2
    print('hurst:', hurst)
    return hurst





def reverting_checker(chunk,samples=10,hurst_lags=2,hurst_timeseries=50):
    list_df = [ts['Close'][i:i + chunk] for i in range(0, ts.shape[0], chunk)]

    ts_close = np.random.choice(list_df,size=samples,replace=True)
    total_hurst = map(ts_close,lambda x: hurst(hurst_lags,hurst_timeseries,x))
    return total_hurst


total_hurst = reverting_checker(60)

#if you want it to cumulate, just append with another one.
total_hurst = total_hurst.append(reverting_checker(60))