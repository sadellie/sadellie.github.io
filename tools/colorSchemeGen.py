import re


def get_arbitrary(
        style: list[str],
        scheme: str,
        color: str,
) -> str:
    styleLine: str = ""
    for line in style:
        if scheme in line:
            if f"-{color}:" in line:
                styleLine = line
                break

    if styleLine == "":
        raise Exception(f"{scheme}, {color} not found")
    rgba = styleLine.split(":")[1]
    numbers = [float(x) for x in re.findall(r'\b\d+\b', rgba)]
    arbitrary = f"rgb({int(numbers[0])},{int(numbers[1])},{int(numbers[2])})"
    return arbitrary


def bg_arb(
        style: list[str],
        scheme: str,
        color: str,
) -> str:
    return f"bg-[{get_arbitrary(style, scheme, color)}]"


def hover_bg_arb(
        style: list[str],
        scheme: str,
        color: str,
) -> str:
    return f"hover:bg-[{get_arbitrary(style, scheme, color)}]/[0.08]"


def group_hover_bg_arb(
        style: list[str],
        scheme: str,
        color: str,
) -> str:
    return f"group-hover:bg-[{get_arbitrary(style, scheme, color)}]/[0.08]"


def text_arb(
        style: list[str],
        scheme: str,
        color: str,
) -> str:
    return f"text-[{get_arbitrary(style, scheme, color)}]"


def border_arb(
        style: list[str],
        scheme: str,
        color: str,
) -> str:
    return f"border-[{get_arbitrary(style, scheme, color)}]"


if __name__ == '__main__':
    all_styles: list[str] = open("indexxo.css").readlines()
    scheme = "dark"

    colorScheme = {
        "primary":                              bg_arb(all_styles, scheme, "primary"),
        "primaryHover":                         hover_bg_arb(all_styles, scheme, "primary"),
        "primaryGroupHover":                    group_hover_bg_arb(all_styles, scheme, "primary"),

        "surfaceTint":                          bg_arb(all_styles, scheme, "surface-tint"),
        "surfaceTintHover":                     hover_bg_arb(all_styles, scheme, "surface-tint"),
        "surfaceTintGroupHover":                group_hover_bg_arb(all_styles, scheme, "surface-tint"),

        "onPrimary":                            bg_arb(all_styles, scheme, "on-primary"),
        "onPrimaryHover":                       hover_bg_arb(all_styles, scheme, "on-primary"),
        "onPrimaryGroupHover":                  group_hover_bg_arb(all_styles, scheme, "on-primary"),
        "onPrimaryText":                        text_arb(all_styles, scheme, "on-primary"),

        "primaryContainer":                     bg_arb(all_styles, scheme, "primary-container"),
        "primaryContainerHover":                hover_bg_arb(all_styles, scheme, "primary-container"),
        "primaryContainerGroupHover":           group_hover_bg_arb(all_styles, scheme, "primary-container"),

        "onPrimaryContainer":                   bg_arb(all_styles, scheme, "on-primary-container"),
        "onPrimaryContainerHover":              hover_bg_arb(all_styles, scheme, "on-primary-container"),
        "onPrimaryContainerGroupHover":         group_hover_bg_arb(all_styles, scheme, "on-primary-container"),
        "onPrimaryContainerText":               text_arb(all_styles, scheme, "on-primary-container"),

        "secondary":                            bg_arb(all_styles, scheme, "secondary"),
        "secondaryHover":                       hover_bg_arb(all_styles, scheme, "secondary"),
        "secondaryGroupHover":                  group_hover_bg_arb(all_styles, scheme, "secondary"),

        "onSecondary":                          bg_arb(all_styles, scheme, "on-secondary"),
        "onSecondaryHover":                     hover_bg_arb(all_styles, scheme, "on-secondary"),
        "onSecondaryGroupHover":                group_hover_bg_arb(all_styles, scheme, "on-secondary"),
        "onSecondaryText":                      text_arb(all_styles, scheme, "on-secondary"),

        "secondaryContainer":                   bg_arb(all_styles, scheme, "secondary-container"),
        "secondaryContainerHover":              hover_bg_arb(all_styles, scheme, "secondary-container"),
        "secondaryContainerGroupHover":         group_hover_bg_arb(all_styles, scheme, "secondary-container"),

        "onSecondaryContainer":                 bg_arb(all_styles, scheme, "on-secondary-container"),
        "onSecondaryContainerHover":            hover_bg_arb(all_styles, scheme, "on-secondary-container"),
        "onSecondaryContainerGroupHover":       group_hover_bg_arb(all_styles, scheme, "on-secondary-container"),
        "onSecondaryContainerText":             text_arb(all_styles, scheme, "on-secondary-container"),

        "tertiary":                             bg_arb(all_styles, scheme, "tertiary"),
        "tertiaryHover":                        hover_bg_arb(all_styles, scheme, "tertiary"),
        "tertiaryGroupHover":                   group_hover_bg_arb(all_styles, scheme, "tertiary"),

        "onTertiary":                           bg_arb(all_styles, scheme, "on-tertiary"),
        "onTertiaryHover":                      hover_bg_arb(all_styles, scheme, "on-tertiary"),
        "onTertiaryGroupHover":                 group_hover_bg_arb(all_styles, scheme, "on-tertiary"),
        "onTertiaryText":                       text_arb(all_styles, scheme, "on-tertiary"),

        "tertiaryContainer":                    bg_arb(all_styles, scheme, "tertiary-container"),
        "tertiaryContainerHover":               hover_bg_arb(all_styles, scheme, "tertiary-container"),
        "tertiaryContainerGroupHover":          group_hover_bg_arb(all_styles, scheme, "tertiary-container"),

        "onTertiaryContainer":                  bg_arb(all_styles, scheme, "on-tertiary-container"),
        "onTertiaryContainerHover":             hover_bg_arb(all_styles, scheme, "on-tertiary-container"),
        "onTertiaryContainerGroupHover":        group_hover_bg_arb(all_styles, scheme, "on-tertiary-container"),
        "onTertiaryContainerText":              text_arb(all_styles, scheme, "on-tertiary-container"),

        "error":                                bg_arb(all_styles, scheme, "error"),
        "errorHover":                           hover_bg_arb(all_styles, scheme, "error"),
        "errorGroupHover":                      group_hover_bg_arb(all_styles, scheme, "error"),

        "onError":                              bg_arb(all_styles, scheme, "on-error"),
        "onErrorHover":                         hover_bg_arb(all_styles, scheme, "on-error"),
        "onErrorGroupHover":                    group_hover_bg_arb(all_styles, scheme, "on-error"),
        "onErrorText":                          text_arb(all_styles, scheme, "on-error"),

        "errorContainer":                       bg_arb(all_styles, scheme, "error-container"),
        "errorContainerHover":                  hover_bg_arb(all_styles, scheme, "error-container"),
        "errorContainerGroupHover":             group_hover_bg_arb(all_styles, scheme, "error-container"),

        "onErrorContainer":                     bg_arb(all_styles, scheme, "on-error-container"),
        "onErrorContainerHover":                hover_bg_arb(all_styles, scheme, "on-error-container"),
        "onErrorContainerGroupHover":           group_hover_bg_arb(all_styles, scheme, "on-error-container"),
        "onErrorContainerText":                 text_arb(all_styles, scheme, "on-error-container"),

        "background":                           bg_arb(all_styles, scheme, "background"),
        "backgroundHover":                      hover_bg_arb(all_styles, scheme, "background"),
        "backgroundGroupHover":                 group_hover_bg_arb(all_styles, scheme, "background"),

        "onBackground":                         bg_arb(all_styles, scheme, "on-background"),
        "onBackgroundHover":                    hover_bg_arb(all_styles, scheme, "on-background"),
        "onBackgroundGroupHover":               group_hover_bg_arb(all_styles, scheme, "on-background"),
        "onBackgroundText":                     text_arb(all_styles, scheme, "on-background"),

        "surface":                              bg_arb(all_styles, scheme, "surface"),
        "surfaceHover":                         hover_bg_arb(all_styles, scheme, "surface"),
        "surfaceGroupHover":                    group_hover_bg_arb(all_styles, scheme, "surface"),

        "onSurface":                            bg_arb(all_styles, scheme, "on-surface"),
        "onSurfaceHover":                       hover_bg_arb(all_styles, scheme, "on-surface"),
        "onSurfaceGroupHover":                  group_hover_bg_arb(all_styles, scheme, "on-surface"),
        "onSurfaceText":                        text_arb(all_styles, scheme, "on-surface"),

        "surfaceVariant":                       bg_arb(all_styles, scheme, "surface-variant"),
        "surfaceVariantHover":                  hover_bg_arb(all_styles, scheme, "surface-variant"),
        "surfaceVariantGroupHover":             group_hover_bg_arb(all_styles, scheme, "surface-variant"),

        "onSurfaceVariant":                     bg_arb(all_styles, scheme, "on-surface-variant"),
        "onSurfaceVariantHover":                hover_bg_arb(all_styles, scheme, "on-surface-variant"),
        "onSurfaceVariantGroupHover":           group_hover_bg_arb(all_styles, scheme, "on-surface-variant"),
        "onSurfaceVariantText":                 text_arb(all_styles, scheme, "on-surface-variant"),

        "outline":                              bg_arb(all_styles, scheme, "outline"),
        "outlineHover":                         hover_bg_arb(all_styles, scheme, "outline"),
        "outlineGroupHover":                    group_hover_bg_arb(all_styles, scheme, "outline"),
        "outlineBorder":                        border_arb(all_styles, scheme, "outline"),

        "outlineVariant":                       bg_arb(all_styles, scheme, "outline-variant"),
        "outlineVariantHover":                  hover_bg_arb(all_styles, scheme, "outline-variant"),
        "outlineVariantGroupHover":             group_hover_bg_arb(all_styles, scheme, "outline-variant"),
        "outlineVariantBorder":                 border_arb(all_styles, scheme, "outline-variant"),

        "shadow":                               bg_arb(all_styles, scheme, "shadow"),
        "shadowHover":                          hover_bg_arb(all_styles, scheme, "shadow"),
        "shadowGroupHover":                     group_hover_bg_arb(all_styles, scheme, "shadow"),

        "scrim":                                bg_arb(all_styles, scheme, "scrim"),
        "scrimHover":                           hover_bg_arb(all_styles, scheme, "scrim"),
        "scrimGroupHover":                      group_hover_bg_arb(all_styles, scheme, "scrim"),

        "inverseSurface":                       bg_arb(all_styles, scheme, "inverse-surface"),
        "inverseSurfaceHover":                  hover_bg_arb(all_styles, scheme, "inverse-surface"),
        "inverseSurfaceGroupHover":             group_hover_bg_arb(all_styles, scheme, "inverse-surface"),

        "inverseOnSurface":                     bg_arb(all_styles, scheme, "inverse-on-surface"),
        "inverseOnSurfaceHover":                hover_bg_arb(all_styles, scheme, "inverse-on-surface"),
        "inverseOnSurfaceGroupHover":           group_hover_bg_arb(all_styles, scheme, "inverse-on-surface"),
        "inverseOnSurfaceText":                 text_arb(all_styles, scheme, "inverse-on-surface"),

        "inversePrimary":                       bg_arb(all_styles, scheme, "inverse-primary"),
        "inversePrimaryHover":                  hover_bg_arb(all_styles, scheme, "inverse-primary"),
        "inversePrimaryGroupHover":             group_hover_bg_arb(all_styles, scheme, "inverse-primary"),

        "primaryFixed":                         bg_arb(all_styles, scheme, "primary-fixed"),
        "primaryFixedHover":                    hover_bg_arb(all_styles, scheme, "primary-fixed"),
        "primaryFixedGroupHover":               group_hover_bg_arb(all_styles, scheme, "primary-fixed"),

        "onPrimaryFixed":                       bg_arb(all_styles, scheme, "on-primary-fixed"),
        "onPrimaryFixedHover":                  hover_bg_arb(all_styles, scheme, "on-primary-fixed"),
        "onPrimaryFixedGroupHover":             group_hover_bg_arb(all_styles, scheme, "on-primary-fixed"),
        "onPrimaryFixedText":                   text_arb(all_styles, scheme, "on-primary-fixed"),

        "primaryFixedDim":                      bg_arb(all_styles, scheme, "primary-fixed-dim"),
        "primaryFixedDimHover":                 hover_bg_arb(all_styles, scheme, "primary-fixed-dim"),
        "primaryFixedDimGroupHover":            group_hover_bg_arb(all_styles, scheme, "primary-fixed-dim"),

        "onPrimaryFixedVariant":                bg_arb(all_styles, scheme, "on-primary-fixed-variant"),
        "onPrimaryFixedVariantHover":           hover_bg_arb(all_styles, scheme, "on-primary-fixed-variant"),
        "onPrimaryFixedVariantGroupHover":      group_hover_bg_arb(all_styles, scheme, "on-primary-fixed-variant"),
        "onPrimaryFixedVariantText":            text_arb(all_styles, scheme, "on-primary-fixed-variant"),

        "secondaryFixed":                       bg_arb(all_styles, scheme, "secondary-fixed"),
        "secondaryFixedHover":                  hover_bg_arb(all_styles, scheme, "secondary-fixed"),
        "secondaryFixedGroupHover":             group_hover_bg_arb(all_styles, scheme, "secondary-fixed"),

        "onSecondaryFixed":                     bg_arb(all_styles, scheme, "on-secondary-fixed"),
        "onSecondaryFixedHover":                hover_bg_arb(all_styles, scheme, "on-secondary-fixed"),
        "onSecondaryFixedGroupHover":           group_hover_bg_arb(all_styles, scheme, "on-secondary-fixed"),
        "onSecondaryFixedText":                 text_arb(all_styles, scheme, "on-secondary-fixed"),

        "secondaryFixedDim":                    bg_arb(all_styles, scheme, "secondary-fixed-dim"),
        "secondaryFixedDimHover":               hover_bg_arb(all_styles, scheme, "secondary-fixed-dim"),
        "secondaryFixedDimGroupHover":          group_hover_bg_arb(all_styles, scheme, "secondary-fixed-dim"),

        "onSecondaryFixedVariant":              bg_arb(all_styles, scheme, "on-secondary-fixed-variant"),
        "onSecondaryFixedVariantHover":         hover_bg_arb(all_styles, scheme, "on-secondary-fixed-variant"),
        "onSecondaryFixedVariantGroupHover":    group_hover_bg_arb(all_styles, scheme, "on-secondary-fixed-variant"),
        "onSecondaryFixedVariantText":          text_arb(all_styles, scheme, "on-secondary-fixed-variant"),

        "tertiaryFixed":                        bg_arb(all_styles, scheme, "tertiary-fixed"),
        "tertiaryFixedHover":                   hover_bg_arb(all_styles, scheme, "tertiary-fixed"),
        "tertiaryFixedGroupHover":              group_hover_bg_arb(all_styles, scheme, "tertiary-fixed"),

        "onTertiaryFixed":                      bg_arb(all_styles, scheme, "on-tertiary-fixed"),
        "onTertiaryFixedHover":                 hover_bg_arb(all_styles, scheme, "on-tertiary-fixed"),
        "onTertiaryFixedGroupHover":            group_hover_bg_arb(all_styles, scheme, "on-tertiary-fixed"),
        "onTertiaryFixedText":                  text_arb(all_styles, scheme, "on-tertiary-fixed"),

        "tertiaryFixedDim":                     bg_arb(all_styles, scheme, "tertiary-fixed-dim"),
        "tertiaryFixedDimHover":                hover_bg_arb(all_styles, scheme, "tertiary-fixed-dim"),
        "tertiaryFixedDimGroupHover":           group_hover_bg_arb(all_styles, scheme, "tertiary-fixed-dim"),

        "onTertiaryFixedVariant":               bg_arb(all_styles, scheme, "on-tertiary-fixed-variant"),
        "onTertiaryFixedVariantHover":          hover_bg_arb(all_styles, scheme, "on-tertiary-fixed-variant"),
        "onTertiaryFixedVariantGroupHover":     group_hover_bg_arb(all_styles, scheme, "on-tertiary-fixed-variant"),
        "onTertiaryFixedVariantText":           text_arb(all_styles, scheme, "on-tertiary-fixed-variant"),

        "surfaceDim":                           bg_arb(all_styles, scheme, "surface-dim"),
        "surfaceDimHover":                      hover_bg_arb(all_styles, scheme, "surface-dim"),
        "surfaceDimGroupHover":                 group_hover_bg_arb(all_styles, scheme, "surface-dim"),

        "surfaceBright":                        bg_arb(all_styles, scheme, "surface-bright"),
        "surfaceBrightHover":                   hover_bg_arb(all_styles, scheme, "surface-bright"),
        "surfaceBrightGroupHover":              group_hover_bg_arb(all_styles, scheme, "surface-bright"),

        "surfaceContainerLowest":               bg_arb(all_styles, scheme, "surface-container-lowest"),
        "surfaceContainerLowestHover":          hover_bg_arb(all_styles, scheme, "surface-container-lowest"),
        "surfaceContainerLowestGroupHover":     group_hover_bg_arb(all_styles, scheme, "surface-container-lowest"),

        "surfaceContainerLow":                  bg_arb(all_styles, scheme, "surface-container-low"),
        "surfaceContainerLowHover":             hover_bg_arb(all_styles, scheme, "surface-container-low"),
        "surfaceContainerLowGroupHover":        group_hover_bg_arb(all_styles, scheme, "surface-container-low"),

        "surfaceContainer":                     bg_arb(all_styles, scheme, "surface-container"),
        "surfaceContainerHover":                hover_bg_arb(all_styles, scheme, "surface-container"),
        "surfaceContainerGroupHover":           group_hover_bg_arb(all_styles, scheme, "surface-container"),

        "surfaceContainerHigh":                 bg_arb(all_styles, scheme, "surface-container-high"),
        "surfaceContainerHighHover":            hover_bg_arb(all_styles, scheme, "surface-container-high"),
        "surfaceContainerHighGroupHover":       group_hover_bg_arb(all_styles, scheme, "surface-container-high"),

        "surfaceContainerHighest":              bg_arb(all_styles, scheme, "surface-container-highest"),
        "surfaceContainerHighestHover":         hover_bg_arb(all_styles, scheme, "surface-container-highest"),
        "surfaceContainerHighestGroupHover":    group_hover_bg_arb(all_styles, scheme, "surface-container-highest"),
    }

    for key in colorScheme:
        print(f"{key}: \"{colorScheme[key]}\",")
