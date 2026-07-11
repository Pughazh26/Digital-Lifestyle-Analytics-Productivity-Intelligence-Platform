-- Average lifestyle metrics by screen time band.
SELECT
    screen_time_band,
    ROUND(AVG(screen_time_hours), 2) AS avg_screen_time,
    ROUND(AVG(sleep_hours), 2) AS avg_sleep,
    ROUND(AVG(exercise_minutes), 2) AS avg_exercise_minutes,
    ROUND(AVG(focus_score), 2) AS avg_focus_score,
    ROUND(AVG(wellbeing_score), 2) AS avg_wellbeing_score
FROM digital_lifestyle_metrics
GROUP BY screen_time_band
ORDER BY avg_wellbeing_score DESC;

-- Weekend versus weekday productivity.
SELECT
    is_weekend,
    ROUND(AVG(productive_ratio), 3) AS avg_productive_ratio,
    ROUND(AVG(social_media_hours), 2) AS avg_social_media_hours,
    ROUND(AVG(focus_score), 2) AS avg_focus_score
FROM digital_lifestyle_metrics
GROUP BY is_weekend;

-- Best days by wellbeing score.
SELECT
    date,
    day_name,
    wellbeing_score,
    focus_score,
    sleep_hours,
    exercise_minutes
FROM digital_lifestyle_metrics
ORDER BY wellbeing_score DESC
LIMIT 10;
