import jenkins
import flask

jenkins_routes = flask.Blueprint(name='jenkins',import_name=__name__,url_prefix='/jenkins')

@jenkins_routes.route('/')
def index():
    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    try:
        client = jenkins.Jenkins('http://localhost:8081',username='admin',password='admin')
        jobs_list = client.get_jobs()
        jobs = []

        for job in jobs_list:
            jobs.append(client.get_job_info(job['fullname']))
    except Exception as e:
        print(e)
        jobs = []
        
    return flask.render_template('jenkins.jinja',jobs=jobs)

@jenkins_routes.route('/build/<string:job_name>')
def jenkins_build(job_name):
    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    try:
        client = jenkins.Jenkins('http://localhost:8081',username='admin',password='admin')
        client.build_job(job_name)
    except Exception as e:
        print(e)
    return flask.redirect(flask.url_for('jenkins.index'))
    
@jenkins_routes.route('/update/<string:job_name>')
def jenkins_update(job_name):
    try:
        client = jenkins.Jenkins('http://localhost:8081',username='admin',password='admin')
        job = {
            'name': job_name,
            'xml': client.get_job_config(job_name)
        }
    except Exception as e:
        print(e)
    return flask.render_template('jenkins_update.jinja',job=job)

@jenkins_routes.route('/rebuild', methods=['POST'])
def jenkins_rebuild():
    data = flask.request.form
    try:
        client = jenkins.Jenkins('http://localhost:8081',username='admin',password='admin')
        client.reconfig_job(data['name'],data['xml'])
        return flask.redirect(flask.url_for('jenkins.index'))
    except Exception:
        return flask.redirect(flask.url_for('jenkins.update', job_name=data['name']))