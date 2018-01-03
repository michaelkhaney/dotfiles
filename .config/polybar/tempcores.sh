#!/bin/bash

# fork from Per-core temperatures :
# https://github.com/jaagr/polybar/wiki/User-contributed-modules#per-core-temperatures

# Get information from cores temp thanks to sensors
rawData=$( sensors | grep acpitz -A 2 | grep C | awk '{print substr($2, 2, length($2)-5)}' )
# rawData=$( sensors | grep Core | awk '{print substr($3, 2, length($3)-5)}' )
tempCore=($rawData)

# Define constants :
# degree="°"
temperaturesValues=(30 45 52 80 100 200)
temperaturesColors=("#9fc59f" "#fff496" "#ff9f5f" "#ff5050" "#e60000" "#ef02db")
# temperaturesColors=("#6bff49" "#f4cb24" "#ff8819" "#ff3205" "#f40202" "#ef02db")
temperaturesIcons=(     )

for iCore in ${!tempCore[*]}
do
    for iTemp in ${!temperaturesValues[*]}
    do
        if (( "${tempCore[$iCore]}" < "${temperaturesValues[$iTemp]}"  )); then
            tmpEcho="%{F#dcdccc}${tempCore[$iCore]}$degree%{F-}"
            finalEcho="$finalEcho $tmpEcho"
            break
        fi
    done
    total=$(( ${tempCore[$iCore]} + total ));
done

sum=$(( $total/${#tempCore[*]} ))

for iTemp in ${!temperaturesValues[*]}
do
    if (( "$sum" < "${temperaturesValues[$iTemp]}" )); then
        ## Decide if you want the icon colored too, default isn't
        tmpEcho="%{F${temperaturesColors[$iTemp]}}${temperaturesIcons[$iTemp]}%{F-}"
        # tmpEcho="%{F${temperaturesColors[$iTemp]}}%{F#6f6f6f}${temperaturesIcons[$iTemp]}%{F-}"
        # tmpEcho="${temperaturesIcons[$iTemp]}"
        finalEcho="$tmpEcho $finalEcho"
        break
    fi
done

echo $finalEcho
