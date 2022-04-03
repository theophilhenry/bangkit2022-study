<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Modifying and Testing Manifests <hr/>
How to make sure, you don't broke anything, before automatically applying the changes to the fleet?

- `Puppet Parser Validate` : Check syntax of the manifest is correct.

- `--noop` : No Operations, simulate what it would do without actually doing it.

- Have a test machine. 

- Have an automatic `rspec` tests. 
```puppet
describe 'gksu', :type => :class do
    let (:facts) {{'is_virtual' => 'false' }}
    it { should_contain('gksu').with_ensure('latest') }
end
```

<br>

## Safely Rolling out Changes and Validating Them <hr/>
- You can create a test env, with its own configuration, different from the production environment.
- Deploy your changes in batches. 
- Small and self contained changes

<br>

Readings :
<ul><li><p><a href="https://rspec-puppet.com/tutorial/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://rspec-puppet.com/tutorial/</u></a></p></li><li><p><a href="http://puppet-lint.com/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>http://puppet-lint.com/</u></a></p></li></ul>



