package test;

import java.util.Optional;

public class Option<T> {

    private Optional<T> opt ;

    public Option(boolean b, T someClass) {
        if (b) {
            this.opt = Optional.ofNullable(someClass);
        }
    }

    public Option() {
        this.opt = Optional.empty();
    }



    public static Option fromValue(SomeClass o) {

        return new Option(true, o);
    }

    public static Option createEmptyOption() {
        return new Option();
    }


    public T getValue() {
        return  opt.orElseThrow(IllegalAccessError::new);

    }

    public boolean hasValue() {
        return opt.isPresent();
    }


    public T valueOrElse(IValueProvider<T> someClassIValueProvider) {
        return opt.isPresent()  ? this.getValue()
                : someClassIValueProvider.getValue();
    }
}
