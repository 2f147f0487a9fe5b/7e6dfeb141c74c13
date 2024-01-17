
#Patches should be in __all__

__all__ = (
    "qualities",
)

#Name variable same as filename
qualities = [
    {
        'expression': '(?<=\"epic\"])()(?=])',
        'value': ',["orange", "legendary"],["red", "mythical"]'
    },
    {
        'expression': '(?<=t=>)()(?=t>=\d+\?\d:)',
        'value': 't>=110?5:t>=99?4:'
    },
    {
        'expression': '(?<=\()(\"\.\")(?=,\"_grey\.\"\))',
        'value': '/(?<!githubusercontent)\.(?!githubusercontent)/'
    },
    {
        'expression': '(/data/items)(?=/\${\w}/\$)',
        'value': 'https://raw.githubusercontent.com/2f147f0487a9fe5b/cb2e2197348007b8/main'
    },
    {
        'expression': '(?<=_q\$\{\w\}\.)(\$\{\w+\})',
        'value': 'webp'
    },
    {
        'expression': '(?<=\"purp\"\),size:20\})',
        'value': ',legendary:{fill:"#EE960B",size:20},mythical:{fill:"#a72929",size:20}'
    }
]